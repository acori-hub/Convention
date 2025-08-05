import java.util.*;
import java.io.*;

public class order_processor {
    private List<String> orders;
    private double totalAmount;
    
    public order_processor() {
        orders = new ArrayList<>();
        totalAmount = 0.0;
    }
    
    // 주문을 추가하는 메소드입니다
    public void addOrder(String orderData) {
        if(orderData != null)
    orders.add(orderData);
    }
    
    public double calculateOrderValue(String order) {
        // TODO: 할인 로직 추가 예정
        String[] parts = order.split(",");
        
        if(parts.length >= 3) {
            try {
                double price = Double.parseDouble(parts[1]);
                int quantity = Integer.parseInt(parts[2]);
                
                double subtotal = price * quantity;
                
                if(quantity > 5)
                    subtotal = subtotal * 0.9;
                else if(quantity > 10)
                    subtotal = subtotal * 0.85;
                    
                if(subtotal > 100)
                    subtotal += 15;
                else
                    subtotal += 5;
                    
                return subtotal;
            }
            catch(NumberFormatException e) {
                return 0.0;
            }
        }
        return 0.0;
    }
    
    public void ProcessAllOrders() {
        for(String order : orders) {
            double value = calculateOrderValue(order);
            totalAmount += value;
            System.out.println("Processed order: " + order + " Value: " + value);
        }
        
        if(totalAmount > 500) {
            System.out.println("Large order batch processed");
        }
    }
}

class OrderTest {
    public static void runTest() {
        order_processor processor = new order_processor();
        
        // 테스트 케이스 1
        processor.addOrder("Item1,50.0,3");
        processor.ProcessAllOrders();
        
        // Test case 2: large quantity
        processor.addOrder("Item2,20.0,8");
        processor.ProcessAllOrders();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        order_processor processor = new order_processor();
        
        System.out.print("Run tests? (y/n): ");
        String choice = scanner.nextLine();
        
        if(choice.equals("y"))
            OrderTest.runTest();
        else {
            System.out.print("Enter order data (item,price,quantity): ");
            String orderData = scanner.nextLine();
            processor.addOrder(orderData);
            processor.ProcessAllOrders();
        }
        
        scanner.close();
    }
}