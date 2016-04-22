package trustresourceallocation;

public class DataCenterCharacteristics {
    private String arch;
    private String os;
    private String vmm;
    private double costperpes;
    private double costpermem;
    private double costperstorage;
    private double costperbw;
	public DataCenterCharacteristics(String arch,String os,String vmm,double costperpes,double costpermem,double costperbw,double costperstorage)
	{
		 setarch(arch);
		 setos(os);
		 setvmm(vmm);
		 setcostperpes(costperpes);
		 setcostpermem(costpermem);
		 setcostperstorage(costperstorage);
		 setcostperbw(costperbw);
		 
		 
	}
	protected void setarch(String arch)
	{
		this.arch=arch;
	}
	protected void setos(String os)
	{
		this.os=os;
	}
	protected void setvmm(String vmm)
	{
		this.vmm=vmm;
	}
	protected void setcostperpes(double costperpes)
	{
		this.costperpes=costperpes;
	}
	protected void setcostpermem(double costpermem)
	{
		this.costpermem=costpermem;
	}
	protected void setcostperstorage(double costperstorage)
	{
		this.costperstorage=costperstorage;
	}
	protected void setcostperbw(double costperbw)
	{
		this.costperbw=costperbw;
	}
	public String getArch()
	{
		return arch;
	}
	public String getOs()
	{
		return os;
	}
	public String getVmm()
	{
		return vmm;
	}
	public double getcostperpes()
	{
		return costperpes;
	}
	public double getcostpermem()
	{
		return costpermem;
	}
	public double getcostperstorage()
	{
		return costperstorage;
	}
	public double getcostperbw()
	{
		return costperbw;
	}
}
