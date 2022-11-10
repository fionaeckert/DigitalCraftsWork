// Create an email client in javascript: Using the node email client of your choice, write a function that sends an email based on the input from a user.
// Hint: You will need a gmail account(or similar) to act as the email server

const nodemailer = require("nodemailer")




async function main(){

    let transporter = nodemailer.createTransport({
        host: "smtp.gmail.com",
        port: 465,
        secure: true,
        auth: {
            user: "fionameckert",
            pass: "aaacubiuzkkdanlx",
        }, 
    });

    let info = await transporter.sendMail({
        from: '"Count Chocula 🧛" <fionameckert@gmail.com>',
        to: '"Boo Berry 👻" <feckert@energy-solution.com>',
        subject: "Frankenberry at it again ... ",
        text: "Can you believe what Frankenberry 🧟 said last night? Unbelievable! Excited to hear your thoughts! \n Xoxo, Choc 🧛",
    });
    console.log("Message sent: %s", info.messageId);
    console.log("Preview URL: %s", nodemailer.getTestMessageUrl(info));
}
main().catch(console.error);