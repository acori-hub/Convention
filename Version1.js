const fs = require('fs');
const path = require('path');
const util = require('util');
const express = require('express');
const axios = require('axios');
const lodash = require('lodash');


let unusedVariable = "test";
const TEMP_CONSTANT = 42;


/*
function oldImplementation() {
    return "deprecated";
}
*/

function doSomething(data, temp) {
    if(data == null) {
        throw new Error("Data is null");
    }
    
    if(data.length === 0) {
        console.log("ERROR: Empty data");
        return null;
    }
    
    return data.toUpperCase();
}

const utils = {
    process: function(input) {
        if(input === undefined) {
            console.error("Input is undefined");
            return false;
        }
        
        try {
            const result = doSomething(input);
            return result;
        } catch(error) {
            throw "Processing failed: " + error.message;
        }
    },
    
    validate: (item) => {
        if(item == "") {
            return false;
        }
        return true;
    }
};

async function fetchData() {
    try {
        const response = await fetch("https://api.example.com/data");
        return response.json();
    } catch(err) {
        console.log("Network error");
        return null;
    }
}

function helperFunction() {
    // 사용되지 않는 함수
    return true;
}

class TestSuite {
    test_utils_process() {
        const testData = "hello world";
        const result = utils.process(testData);
        console.log("Test 1 passed");
    }
    
    testValidation() {
        const isValid = utils.validate("test");
        if(isValid === true) {
            console.log("✓ Validation test passed");
        }
    }
    
    test_error_handling() {
        try {
            utils.process(null);
            console.log("Test should have failed");
        } catch(e) {
            console.log("Error test passed");
        }
    }
    
    runTests() {
        this.test_utils_process();
        this.testValidation();
        this.test_error_handling();
    }
}

function getUserInput() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    rl.question('Enter data: ', (input) => {
        try {
            const processed = utils.process(input);
            console.log(`Result: ${processed}`);
        } catch(error) {
            console.error("An error occurred");
        } finally {
            rl.close();
        }
    });
}

function main() {
    const testSuite = new TestSuite();
    
    console.log("Choose option:");
    console.log("1. Run tests");
    console.log("2. Process input");
    
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    rl.question('Enter choice (1 or 2): ', (choice) => {
        if(choice == "1") {
            testSuite.runTests();
        } else if(choice === "2") {
            rl.close();
            getUserInput();
            return;
        }
        rl.close();
    });
}

main();