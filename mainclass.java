package trustresourceallocation;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;
import org.cloudbus.cloudsim.examples.cloudSim;
import trustresourceallocation.DataCenter;
import java.util.*;
import java.io.*;
import trustresourceallocation.Host;
import trustresourceallocation.Vm;
import trustresourceallocation.DataCenterCharacteristics;

//import org.cloudbus.cloudsim.CloudletSchedulerTimeShared;
import org.cloudbus.cloudsim.Datacenter;
import org.cloudbus.cloudsim.Log;
//import org.cloudbus.cloudsim.Vm;
//import org.cloudbus.cloudsim.VmAllocationPolicySimple;
//import org.cloudbus.cloudsim.VmSchedulerSpaceShared;
import org.cloudbus.cloudsim.core.CloudSim;
import org.cloudbus.cloudsim.provisioners.BwProvisionerSimple;
import org.cloudbus.cloudsim.provisioners.RamProvisionerSimple;
@SuppressWarnings({"unchecked", "deprecation"})
public class mainclass {
	   public static DataCenter createDatacenter(String name)
	   {
		   List<Host> hostList = new ArrayList<Host>();
		 //4. Create Host with its id and list of PEs and add them to the list of machines
			int hostId=0;
			int ram = 10240; //host memory (MB)
			int storage = 10000; //host storage
			int bw = 10000;
			int pes=10000;
			int sec=2;
			hostList.add(
					new Host(
							hostId,
							ram,
							bw,
							storage,
							pes,sec)
					);// This is our first machine
			hostId++;
			int ram2 = 20000; //host memory (MB)
			int storage2 = 20000; //host storage
			int bw2 = 20000;
			int pes2=20000;
			int sec1=2;
			hostList.add(
					new Host(
							hostId,
							ram2,
							bw2,
							storage2,
							pes2,sec1)
					);
			hostId++;
			int ram3 = 7000;//host memory (MB)
			int storage3 = 8000; //host storage
			int bw3 = 7000;
			int pes3=8000;
			int sec3=1;
			hostList.add(
					new Host(
							hostId,
							ram3,
							bw3,
							storage3,
							pes3,sec3)
					);
			hostId++;
			int ram4 = 7000; //host memory (MB)
			int storage4 = 7000; //host storage
			int bw4 = 7000;
			int pes4=7000;
			int sec4=0;
			hostList.add(
					new Host(
							hostId,
							ram4,
							bw4,
							storage4,
							pes4,sec4)
					);
			hostId++;
			int ram5 = 3000; //host memory (MB)
			int storage5 = 3500; //host storage
			int bw5 = 3000;
			int pes5=3000;
			int sec5=0;
			hostList.add(
					new Host(
							hostId,
							ram5,
							bw5,
							storage5,
							pes5,sec5)
					);
			hostId++;
			int ram6 = 5000; //host memory (MB)
			int storage6 = 5000; //host storage
			int bw6 = 5000;
			int pes6=5000;
			int sec6=1;
			hostList.add(
					new Host(
							hostId,
							ram6,
							bw6,
							storage6,
							pes6,sec6)
					);
			hostId++;
			int ram7 = 4000; //host memory (MB)
			int storage7 = 4000; //host storage
			int bw7 = 4500;
			int pes7=4000;
			int sec7=1;
			hostList.add(
					new Host(
							hostId,
							ram7,
							bw7,
							storage7,
							pes7,sec7)
					);
			hostId++;
			int ram8 = 1024; //host memory (MB)
			int storage8 = 1000; //host storage
			int bw8 = 1000;
			int pes8=1000;
			int sec8=0;
			hostList.add(
					new Host(
							hostId,
							ram8,
							bw8,
							storage8,
							pes8,sec8)
					);
			hostId++;
			int ram9 = 2048; //host memory (MB)
			int storage9 = 1000; //host storage
			int bw9 = 1000;
			int pes9=1000;
			int sec9=0;
			hostList.add(
					new Host(
							hostId,
							ram9,
							bw9,
							storage9,
							pes9,sec9)
					);
			hostId++;
			int ram10 = 10240; //host memory (MB)
			int storage10 = 10000; //host storage
			int bw10 = 10000;
			int pes10=10000;
			int sec10=2;
			hostList.add(
					new Host(
							hostId,
							ram10,
							bw10,
							storage10,
							pes10,sec10)
					);
			// 5. Create a DatacenterCharacteristics object that stores the
			//    properties of a data center: architecture, OS, list of
			//    Machines, allocation policy: time- or space-shared, time zone
			//    and its price (G$/Pe time unit).
			String arch = "x86";      // system architecture
			String os = "Linux";          // operating system
			String vmm = "Xen";
			double cost = 3.0;              // the cost of using processing in this resource
			double costPerMem = 0.05;		// the cost of using memory in this resource
			double costPerStorage = 0.001;	// the cost of using storage in this resource
			double costPerBw = 0.0;			// the cost of using bw in this resource
		    double costPerPes=1.0;          // the cost of using process cycle
		    DataCenterCharacteristics characteristics = new DataCenterCharacteristics(
	                arch, os, vmm,costPerPes, costPerMem, costPerStorage, costPerBw);
		    DataCenter datacenter = null;
		    try {
				datacenter = new DataCenter(name, characteristics, hostList);
			} catch (Exception e) {
				e.printStackTrace();
			}
		    return datacenter;
	   }
       public static void main(String args[])
       {
    	   Log.printLine("Starting Mainclass...");
    	   try {
    		   int num_user = 2;   // number of cloud users
   			Calendar calendar = Calendar.getInstance();
   			boolean trace_flag = false;  // mean trace events

   			// Initialize the CloudSim library
   			
   			CloudSim.init(num_user, calendar, trace_flag);
   			DataCenter ds=createDatacenter("datacenter1");
   			DataCenterBroker bk=new DataCenterBroker("broker1",ds);
   		//VM description
			int vmid = 1;
			int mips = 1000;
			int storage = 1000 ; //image size (MB)
			int ram = 1000; //vm memory (MB)
			int bw = 1000;
		    
            cloudSim.startSimulation();
                       
            bk.monitor();
            //bk.deallocatehost();
		    Vm vm1=new Vm(vmid,mips,ram,bw,storage);
            vmid++;
            bk.bindvmtohost(vm1);
            bk.deallocatehost();
            bk.monitor();
            //bk.deallocatehost();
            Vm vm2=new Vm(vmid,mips,ram,bw,storage);
            vmid++;
            bk.bindvmtohost(vm2);
            bk.deallocatehost();
            bk.monitor();
            Vm vm3=new Vm(vmid,mips,ram,bw,storage);
            vmid++;
            bk.bindvmtohost(vm3);
            bk.deallocatehost();
            bk.monitor();
            bk.deallocatehost();
            bk.showmapping();
            //bk.monitor();
            //bk.bindvmtohost(vmlist1);
            System.out.println("user services sucessfully allocated");
   			
            System.out.println("resource deallocated");
            
            cloudSim.stopsimulation();
   			//bk.deallocatehost();
   			
    	   }
    	   catch(Exception e)
    	   {
    		   System.err.println(e);
    	   }
    	   

       }
}
