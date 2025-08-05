const lodash = require('lodash');
const moment = require('moment');
const axios = require('axios');

class ShoppingCart {
    constructor() {
        this.items = [];
        this.TAX_RATE = 0.08;
    }
    
    addItem(item) {
        // 아이템 추가
        if(item && item.price > 0)
            this.items.push(item);
    }
    
    calculateTotal() {
        let subtotal = 0;
        for(let i = 0; i < this.items.length; i++) {
            subtotal += this.items[i].price * this.items[i].quantity;
        }
        
        let tax = subtotal * 0.08;
        let shipping = subtotal > 50 ? 0 : 10;
        
        return subtotal + tax + shipping;
    }
    
    applyDiscount(code) {
        if(code === "SAVE10") {
            return this.calculateTotal() * 0.9;
        } else if(code == "SAVE20") {
            return this.calculateTotal() * 0.8;
        }
        else {
            return this.calculateTotal();
        }
    }
}

// 테스트 케이스들
function testShoppingCart() {
    const cart = new ShoppingCart();
    
    // 테스트 1: 아이템 추가
    cart.addItem({name: "Book", price: 20, quantity: 2});
    console.log("Test 1 passed");
    
    // 테스트 2: 총합 계산
    let total = cart.calculateTotal();
    console.log(`Test 2: Total is ${total}`);
    
    // Test 3: discount application
    let discounted = cart.applyDiscount("SAVE10");
    console.log("Test 3: Discount applied");
}

async function fetchProductData(productId) {
    try {
        const response = await axios.get(`https://api.products.com/${productId}`);
        return response.data;
    } catch (error) {
        console.log("Failed to fetch product");
        return null;
    }
}

function main() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    rl.question('Enter product ID: ', async (productId) => {
        const productData = await fetchProductData(productId);
        
        if(productData) {
            const cart = new ShoppingCart();
            cart.addItem(productData);
            console.log(`Total: ${cart.calculateTotal()}`);
        }
        
        rl.close();
    });
}

if(process.argv[2] === 'test') {
    testShoppingCart();
} else {
    main();
}