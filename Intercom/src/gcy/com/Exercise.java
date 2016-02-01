package gcy.com;
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Collections;
import org.json.simple.parser.ContainerFactory;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class Exercise {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Customer> result = new ArrayList<Customer>();
        try {
			File file = new File("src/gcy/com/text.txt");
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);
			String s = "";
			while((s = br.readLine()) != null){
				JSONParser parser = new JSONParser();
				ContainerFactory containerFactory = new ContainerFactory(){
				    public List creatArrayContainer() {
				      return new LinkedList();
				    }
				    public Map createObjectContainer() {
				      return new LinkedHashMap();
				    }				                        
				  };
				  try {
					Map json = (Map) parser.parse(s,containerFactory);
					Iterator iter = json.entrySet().iterator();
				  
					List<String> info = new ArrayList<String>();
					while(iter.hasNext()){												
						Map.Entry entry = (Map.Entry)iter.next();
						info.add( entry.getValue().toString());	
					}
					Customer c = new Customer();
					double latitude = Double.parseDouble(info.get(0));
					int id = Integer.parseInt(info.get(1));
					String name = info.get(2);
					double longitude = Double.parseDouble(info.get(3));
					c.setLatitude(latitude);
					c.setID(id);
					c.setName(name);
					c.setLongitude(longitude);
					double dis = c.getDistance(latitude, longitude);
					if(dis >=0 && dis <= 100)
						result.add(c);					
				  }		  
				 catch (ParseException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}				
			}
			br.close();
			fr.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}         
         Collections.sort(result); 
         for(int i = 0;i<result.size();i++){
        	 System.out.println(result.get(i).getID() + "\t" + result.get(i).getName());
         }	
	}
}