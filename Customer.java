package gcy.com;

public class Customer implements Comparable<Customer> {
    private int ID;
    private String name;
    private double latitude;
    private double longitude;
    public int getID() {
		return ID;
	}
	public void setID(int iD) {
		ID = iD;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public double getLatitude() {
		return latitude;
	}
	public void setLatitude(double latitude) {
		this.latitude = latitude;
	}
	public double getLongitude() {
		return longitude;
	}
	public void setLongitude(double longitude) {
		this.longitude = longitude;
	}
	
   
    public Customer(double lt,int ID,String name,double lg){
    	this.ID = ID;
    	this.name = name;
    	this.latitude = lt;
    	this.longitude = lg;
    }
    public Customer(){
    	
    }
    public double getDistance(double latitude,double longitude){
    	double difOfLat =  Math.toRadians(Math.abs(latitude -  53.3381985));
    	double difOfLon =  Math.toRadians(Math.abs(longitude + 6.2592576));   	
    	double df = 2  * Math.asin(Math.sqrt(Math.sin(difOfLat / 2) * 
    			Math.sin(difOfLat) + Math.cos(Math.toRadians(latitude)) * 
    			Math.cos(Math.toRadians(53.3381985))*
    			Math.sin(difOfLon / 2) * Math.sin(difOfLon / 2))) ;
    	double distance = 6371 * df;
    	return distance;
    }
	@Override	
	public int compareTo(Customer c) {
		// TODO Auto-generated method stub
		if(this.ID > c.ID){
			return 1;
		}
		else if (this.ID < c.ID){
			return -1;
		}else {
			return 0;
		}
		
	}
}	

