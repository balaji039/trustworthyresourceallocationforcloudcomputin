package trustresourceallocation;
import java.util.*;
import trustresourceallocation.Host;
import trustresourceallocation.DataCenterCharacteristics;
public class DataCenter {
	   private String name;
	   private DataCenterCharacteristics characteristics;
	   private List<Host> hostlist;
       public DataCenter(String name,DataCenterCharacteristics characteristics,List<Host> hostlist)
       {
    	   setname(name);
    	   setdatacharacteristics(characteristics);
    	   sethostdetails(hostlist);
       }
       public void setname(String name)
       {
    	   this.name=name;
    	   
       }
       public void setdatacharacteristics(DataCenterCharacteristics characteristics)
       {
    	   this.characteristics=characteristics;
       }
       public void sethostdetails(List<Host> hostlist)
       {
    	   this.hostlist=hostlist;
       }
       public List<Host> gethostinfo()
       {
    	   return hostlist;
       }
       public DataCenterCharacteristics getdatacharacteristics()
       {
    	   return characteristics;
    	   
       }
       public String getname()
       {
    	   return name;
       }
}
