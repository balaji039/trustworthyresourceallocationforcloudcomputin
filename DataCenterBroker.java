package trustresourceallocation;
import java.util.*;
import java.util.Map.Entry;
import java.io.*;
import trustresourceallocation.Vm;

import trustresourceallocation.Host;
import trustresourceallocation.DataCenter;
import trustresourceallocation.DataCenterCharacteristics;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
@SuppressWarnings({"unchecked", "deprecation"})
public class DataCenterBroker {
	private Connection connect = null;
	  private Statement statement = null;
	  private PreparedStatement preparedStatement = null;
	  private PreparedStatement preparedStatement1 = null;
	  private ResultSet resultSet = null;
      private static double count=0.0;
	     private String name;
	     private DataCenter ds;
	     private Map<Vm,Host> mp;
         public DataCenterBroker(String name,DataCenter ds)
         {
        	 this.name=name;
        	 this.ds=ds;
        	 mp=new HashMap<Vm,Host>();
         }
         public int available(int id,Vm hs)
         {
        	 List<Host> hostlist=ds.gethostinfo();
        	 int p=hs.getProcess();
    		    int r=hs.getRam();
    		    int s=hs.getStorage();
    		    int b=hs.getBw();
    	        int tp=hostlist.get(id).getProcess();
    	        int tr=hostlist.get(id).getRam();
    	        int ts=hostlist.get(id).getStorage();
    	        int tb=hostlist.get(id).getBw();
    	     if(tp>p && tr>r && ts>s && tb>b)
    	     {
  	              return 1;
    	     }
    	     else
    	     {
    	    	 return 0;
    	     }
    	     
         }
         public void showmapping()
         {
        	 for (Entry<Vm, Host> entry : mp.entrySet()) {
        		    System.out.println("VM  " + entry.getKey() + ", Host = " + entry.getValue());
        		}        	 
         }
          
         @SuppressWarnings({"unchecked", "deprecation"})
         public void bindvmtohost(Vm hs)
         { 
        	 int id=0;
        	 try
        	 {
        	 Class.forName("com.mysql.jdbc.Driver");
   	      // Setup the connection with the DB
   	         connect = DriverManager
   	          .getConnection("jdbc:mysql://localhost/cloud?useSSL=false","system","system123");
   	           statement = connect.createStatement();
   	           String sql = "SELECT * from trustcloud where trustvalue='HIGH'";
   	           ResultSet rs = statement.executeQuery(sql);
   	      //STEP 5: Extract data from result set
   	            while(rs.next()){
   	         //Retrieve by column name
   	               id  = rs.getInt("cloudserviceid");
   	               //System.out.println(id);
   	               //System.out.println(id+"entering");
   	               if(available(id,hs)==1)
   	               {
   	            	   break;
   	               }
   	               else
   	               {
   	            	   continue;
   	               }
   	            }
   	           //ListIterator<Vm> vtr=vmlist.listIterator();
   	           List<Host> hostlist=ds.gethostinfo();
   	          
       	        //hostlist.get(0).setProcess(3000);
       	       //ListIterator<Host> htr=hostlist.listIterator();
   	        //while(vtr.hasNext())
       	   //{
       		   //Vm hs=vtr.next();
       		    int p=hs.getProcess();
       		    int r=hs.getRam();
       		    int s=hs.getStorage();
       		    int b=hs.getBw();
       	        int tp=hostlist.get(id).getProcess();
       	        int tr=hostlist.get(id).getRam();
       	        int ts=hostlist.get(id).getStorage();
       	        int tb=hostlist.get(id).getBw();
       	        int up=hostlist.get(id).getUprocess();
       	        int ur=hostlist.get(id).getUram();
       	        int us=hostlist.get(id).getUStorage();
       	        int ub=hostlist.get(id).getUbw();
       	        hostlist.get(id).setProcess(tp-p);
    	        hostlist.get(id).setRam(tr-r);
    	        //System.out.println(ts-s);
    	        hostlist.get(id).setStorage(ts-s);
    	        hostlist.get(id).setBw(tb-b);
    	        hostlist.get(id).setUprocess(p+up);
    	        hostlist.get(id).setUram(r+ur);
    	        hostlist.get(id).setUStorage(s+us);
    	        hostlist.get(id).setUbw(b+ub);


    	        /*int tp1=hostlist.get(1).getProcess();
       	        int tr1=hostlist.get(1).getRam();
       	        int ts1=hostlist.get(1).getStorage();
       	        int tb1=hostlist.get(1).getBw();
       	        int up1=hostlist.get(1).getUprocess();
       	        int ur1=hostlist.get(1).getUram();
       	        int us1=hostlist.get(1).getUStorage();
       	        int ub1=hostlist.get(1).getUbw();
       	        hostlist.get(id).setProcess(tp-1000);
    	        hostlist.get(id).setRam(tr-512);
    	        hostlist.get(id).setStorage(ts-300000);
    	        hostlist.get(id).setBw(tb-4000);
    	        hostlist.get(id).setUprocess(p+1000);
    	        hostlist.get(id).setUram(r+512);
    	        hostlist.get(id).setUStorage(s+300000);
    	        hostlist.get(id).setUbw(b+4000);*/
       		   //writer.println(hs.getProcess()+"  "+hs.getRam()+"  "+hs.getBw()+"  "+hs.getStorage()+"  "+hs.getUprocess()+"  "+hs.getUram()+"  "+hs.getUStorage()+"  "+hs.getUbw());
       		   //System.out.println("################################");   
       		    mp.put(hs, hostlist.get(id));
       		    System.out.println(count+":"+"  Trying to create VM #"+hs.getId()+"in"+ds.getname());
       		    if(count==0.2)
       		    {
       		    	System.out.println(0.3+":"+"  vm #"+hs.getId()+"instantiated in "+ ds.getname()+ "  host #"+id);      		    	
       		    	count=count+0.1;      		    
       		    }
       		    else
       		    {
       		    count=count+0.1;
       		    System.out.println(count+":"+"  vm #"+hs.getId()+"instantiated in "+ ds.getname()+ "  host #"+id);
       		    }
       		    count=count+0.1;  
       	   
        	 }
        	 catch(Exception e)
        	 {
        		 System.err.println(e);
        	 }
        	 
        	 
         }
         @SuppressWarnings({"unchecked", "deprecation"})
         public void deallocatehost()
         {
        	 
        	 try
        	 {
        	 Class.forName("com.mysql.jdbc.Driver");
   	      // Setup the connection with the DB
   	      connect = DriverManager
   	   	          .getConnection("jdbc:mysql://localhost/cloud?useSSL=false","system","system123");
   	          statement = connect.createStatement();
              String sql = "DELETE from rerources";
              statement.executeUpdate(sql);
              String sql1 = "DELETE from trustcloud";
              statement.executeUpdate(sql1);
              String sql2 = "DELETE from security";
              statement.executeUpdate(sql2);
   		        
        	 }
        	 catch(Exception e)
        	 {
        		 System.err.println(e);
        	 }
        	 
         }
         @SuppressWarnings({"unchecked", "deprecation"})
         public void monitor()
         {
        	 List<Host> hostlist=ds.gethostinfo();
        	 //hostlist.get(0).setProcess(3000);
        	 ListIterator<Host> htr=hostlist.listIterator();
        	 
        	 try
             {
	                    
        		 Class.forName("com.mysql.jdbc.Driver");
        	      // Setup the connection with the DB
        	      connect = DriverManager
        	   	          .getConnection("jdbc:mysql://localhost/cloud?useSSL=false","system","system123");

        		 
        		 
        	      preparedStatement = connect.prepareStatement("insert into rerources values (?, ?, ?, ?, ? , ?, ?, ?, ?)");
        		  
        		 
        		 
        		 //PrintWriter writer = new PrintWriter("resourcemonitor.txt", "UTF-8");
        	 while(htr.hasNext())
      	   {
      		   Host hs=htr.next();
      		  
      	      preparedStatement.setInt(1, hs.getProcess());
      	      preparedStatement.setInt(2, hs.getRam());
      	      preparedStatement.setInt(3, hs.getBw());
      	      preparedStatement.setInt(4, hs.getStorage());
      	      preparedStatement.setInt(5, hs.getUprocess());
      	      preparedStatement.setInt(6, hs.getUram());
      	      preparedStatement.setInt(7, hs.getUbw());
      	      preparedStatement.setInt(8, hs.getUStorage());
    	      preparedStatement.setInt(9, hs.getId());
      	      preparedStatement.executeUpdate();
      		   //writer.println(hs.getProcess()+"  "+hs.getRam()+"  "+hs.getBw()+"  "+hs.getStorage()+"  "+hs.getUprocess()+"  "+hs.getUram()+"  "+hs.getUStorage()+"  "+hs.getUbw());
      		   //System.out.println("################################");   
      		   
      	   }
        	
        	  preparedStatement1 = connect.prepareStatement("insert into security values (?, ?)");
    		  
        	  ListIterator<Host> htr1=hostlist.listIterator(); 
     		 //System.out.println("fsfds");
     		 //PrintWriter writer = new PrintWriter("resourcemonitor.txt", "UTF-8");
     	 while(htr1.hasNext())
   	   {
   		   Host hs1=htr1.next();
   		  //System.out.println("enter");
   	     
 	      preparedStatement1.setInt(1, hs1.getId());
 	      preparedStatement1.setInt(2, hs1.getSecurity());
   	      preparedStatement1.executeUpdate();
   		   //writer.println(hs.getProcess()+"  "+hs.getRam()+"  "+hs.getBw()+"  "+hs.getStorage()+"  "+hs.getUprocess()+"  "+hs.getUram()+"  "+hs.getUStorage()+"  "+hs.getUbw());
   		   //System.out.println("################################");   
   		   
   	   }
        	 
        	 
        	 //System.out.println("success");
        	
          	Process p=Runtime.getRuntime().exec("python -W ignore D:\\cloud\\mainaccess.py");
          	BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
          	String result = new String();
          	//System.out.println("entering");
          	while((result = in.readLine()) != null) {
          		   System.out.println(result);
          	}
        	 //preparedStatement.executeUpdate();
        	
           }
        	 catch(Exception e)
        	 {
        		  System.err.println(e);
        	 }
         }
}
