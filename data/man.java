import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;
class man{
public static void main(String[] args) throws Exception{
    String data="[";
    try {

      File myObj = new File("mat.txt");
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
         data+= "'"+myReader.nextLine()+"',";
        
      }
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
    System.out.println(data+"AAPL"+"]");
}}