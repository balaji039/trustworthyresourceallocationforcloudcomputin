package trustresourceallocation;

/*
 * Title: CloudSim Toolkit Description: CloudSim (Cloud Simulation) Toolkit for Modeling and
 * Simulation of Clouds Licence: GPL - http://www.gnu.org/copyleft/gpl.html
 * 
 * Copyright (c) 2009-2012, The University of Melbourne, Australia
 */


import java.util.ArrayList;
import java.util.List;
import trustresourceallocation.DataCenter;
import org.cloudbus.cloudsim.core.CloudSim;
import org.cloudbus.cloudsim.lists.PeList;
import org.cloudbus.cloudsim.provisioners.BwProvisioner;
import org.cloudbus.cloudsim.provisioners.RamProvisioner;

/**
 * Host executes actions related to management of virtual machines (e.g., creation and destruction).
 * A host has a defined policy for provisioning memory and bw, as well as an allocation policy for
 * Pe's to virtual machines. A host is associated to a datacenter. It can host virtual machines.
 * 
 * @author Rodrigo N. Calheiros
 * @author Anton Beloglazov
 * @since CloudSim Toolkit 1.0
 */
public class Host {

	/** The id. */
	private int id;

	/** The storage. */
	private int storage;
	
	private int pemips;

	/** The ram provisioner. */
	private int ram;

	/** The bw provisioner. */
	private int bw;
	
	private int security;
	
	private int uram,ubw,upemips,ustorage;

	/** The allocation policy. */
	//private VmScheduler vmScheduler;

	/** The vm list. */
	

	/** The datacenter where the host is placed. */
	//private Datacenter datacenter;

	/**
	 * Instantiates a new host.
	 * 
	 * @param id the id
	 * @param ramProvisioner the ram provisioner
	 * @param bwProvisioner the bw provisioner
	 * @param storage the storage
	 * @param peList the pe list
	 * @param vmScheduler the vm scheduler
	 */
	public Host(
			int id,
			int ram,
			int bw,
			int storage,
			int pemips,int security) {
		setId(id);
		setRam(ram);
		setBw(bw);
		setStorage(storage);
		setProcess(pemips);
		setUram(1);
		setUStorage(1);
		setUprocess(1);
		setUbw(1);
		setSecurity(security);
	}
	protected void setSecurity(int security)
	{
		this.security=security;
	}
    protected void setUram(int uram)
    {
    	this.uram=uram;
    }
    protected void setUStorage(int ustorage)
    {
    	this.ustorage=ustorage;
    }
	
	protected void setUbw(int ubw)
	{
		this.ubw=ubw;
	}
	protected void setUprocess(int upemips)
    {
    	this.upemips=upemips;
    }
	public int getUram()
	{
		return uram;
	}
	public int getUStorage()
	{
		return ustorage;
	}
	public int getSecurity()
	{
		return security;
	}
	public int getUbw()
	{
		return ubw;
	}
	public int getUprocess()
	{
		return upemips;
	}
	protected void setRam(int ram)
	{
		this.ram=ram;
	}
	protected void setBw(int bw)
	{
		this.bw=bw;
	}
	protected void setProcess(int pemips)
	{
		this.pemips=pemips;
	}
	protected int getProcess()
	{
		return pemips;
	}
	
	

	/**
	 * Gets the machine bw.
	 * 
	 * @return the machine bw
	 * @pre $none
	 * @post $result > 0
	 */
	public int getBw()
	{
		return bw;
	}

	/**
	 * Gets the machine memory.
	 * 
	 * @return the machine memory
	 * @pre $none
	 * @post $result > 0
	 */
	public int getRam() {
		return ram;
	}

	/**
	 * Gets the machine storage.
	 * 
	 * @return the machine storage
	 *  $none
	 * @post $result >= 0
	 */
	public int getStorage() {
		return storage;
	}

	/**
	 * Gets the id.
	 * 
	 * @return the id
	 */
	public int getId() {
		return id;
	}

	/**
	 * Sets the id.
	 * 
	 * @param id the new id
	 */
	protected void setId(int id) {
		this.id = id;
	}

	
	
	/**
	 * Sets the storage.
	 * 
	 * @param storage the new storage
	 */
	protected void setStorage(int storage) {
		this.storage = storage;
	}

}
