let savedPassword = {"Facebook": 123};

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function show_passwords(){
    if (Object.keys(savedPassword).length === 0){
        console.log("You don't have any saved passwords.")
    } else {
        console.log("Hi! These are your saved passwords:\n")

        for (pass in savedPassword){
            console.log(pass)
        }

        rl.question('\nWhich password do you want to show?\n\n', (userInput) => {
            let chosen_pass = userInput

            if (savedPassword[chosen_pass]){
                console.log(`\nName: ${chosen_pass}\nPassword: ${savedPassword[chosen_pass]}`)
            } else {
                console.log("Password name not found.")
            }

            rl.close();
        });

        
    }
};


show_passwords()