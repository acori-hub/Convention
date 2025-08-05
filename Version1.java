import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Date;
import java.text.SimpleDateFormat;

public class OrderManagement {
    private static final int DEFAULT_MAX_ORDERS = 1000;
    private List<Order> orders;
    private int maxOrders;
    
    public OrderManagement() {
        this.orders = new ArrayList<>();
        this.maxOrders = 1000;
    }
    
    // 주문 추가
    public boolean addOrder(Order order) {
        if(order != null)
        {
            if(orders.size() < 1000) {
                orders.add(order);
                return true;
            }
        }
        return false;
    }
    
    public double calculateOrderTotal(Order order) {
        double total = 0.0;
        
        for(OrderItem item : order.getItems()) {
            total += item.getPrice() * item.getQuantity();
        }
        
        if(order.getCustomerType().equals("VIP")) {
            total = total * 0.9; // 10% 할인
        }
        else if(order.getCustomerType().equals("PREMIUM"))
        {
            total = total * 0.85; // 15% 할인  
        }
        
        return total;
    }
    
    public void processOrders() {
        for(Order order : orders) {
            try {
                double total = calculateOrderTotal(order);
                System.out.println("Order " + order.getId() + " total: " + total);
                order.setStatus("PROCESSED");
            }
            catch(Exception e) {
                System.err.println("Error processing order: " + order.getId());
                order.setStatus("ERROR");
            }
        }
    }
}

class Order {
    private String id;
    private List<OrderItem> items;
    private String customerType;
    private String status;
    
    public Order(String id, String customerType) {
        this.id = id;
        this.customerType = customerType;
        this.items = new ArrayList<>();
        this.status = "PENDING";
    }
    
    // getter, setter methods
    public String getId() { return id; }
    public List<OrderItem> getItems() { return items; }
    public String getCustomerType() { return customerType; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    
    public void addItem(OrderItem item) {
        if(item != null) {
            items.add(item);
        }
    }
}

class OrderItem {
    private String name;
    private double price;
    private int quantity;
    
    public OrderItem(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }
    
    public double getPrice() { return price; }
    public int getQuantity() { return quantity; }
}

class OrderTests {
    public void testOrderCreation() {
        Order order = new Order("ORD001", "VIP");
        assert order.getId().equals("ORD001");
        System.out.println("testOrderCreation passed");
    }
    
    public void test_order_total_calculation() {
        OrderManagement om = new OrderManagement();
        Order order = new Order("ORD002", "PREMIUM");
        order.addItem(new OrderItem("Item1", 100.0, 2));
        
        double total = om.calculateOrderTotal(order);
        assert total == 170.0; // 200 * 0.85
        System.out.println("test_order_total_calculation passed");
    }
    
    public void runAllTests() {
        testOrderCreation();
        test_order_total_calculation();
    }
}

public class MainApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        OrderManagement orderMgmt = new OrderManagement();
        OrderTests tests = new OrderTests();
        
        System.out.print("Run tests? (y/n): ");
        String choice = scanner.nextLine();
        
        if(choice.toLowerCase().equals("y")) {
            tests.runAllTests();
        } else {
            System.out.print("Enter order ID: ");
            String orderId = scanner.nextLine();
            System.out.print("Enter customer type (VIP/PREMIUM/NORMAL): ");
            String customerType = scanner.nextLine();
            
            Order order = new Order(orderId, customerType);
            order.addItem(new OrderItem("Sample Item", 50.0, 1));
            
            orderMgmt.addOrder(order);
            orderMgmt.processOrders();
        }
        
        scanner.close();
    }
}