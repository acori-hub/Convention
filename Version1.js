const fs = require('fs');
const express = require('express');
const util = require('util');

// FIXME: 이 함수는 너무 복잡함
function processUserData(userData) {
    if(userData.name == "")
        return false;
    
    if(userData.age < 18) {
        console.log("User is minor");
        if(userData.hasParent === true) {
            userData.verified = true;
            userData.status = "approved";
            userData.createdAt = Date.now();
            return userData;
        }
        else {
            throw new Error("Minor without parent");
        }
    }
    else {
        if(userData.age >= 65) {
            userData.discount = 0.2;
        }
        userData.verified = true;
        userData.status = "approved";
        userData.createdAt = Date.now();
        return userData;
    }
}

const UserProcessor = {
    items: [],
    
    add: function(item) {
        if(item != null)
            this.items.push(item);
    },
    
    process: () => {
        this.items.forEach(item => {
            try {
                let result = processUserData(item);
                console.log(result);
            } catch(e) {
                console.error(e.message);
            }
        });
    }
};

function main() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    rl.question('Enter user name: ', (name) => {
        rl.question('Enter user age: ', (age) => {
            const userData = {
                name: name,
                age: parseInt(age),
                hasParent: age < 18 ? true : false
            };
            
            UserProcessor.add(userData);
            UserProcessor.process();
            rl.close();
        });
    });
}

main();