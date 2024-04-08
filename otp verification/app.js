// Initialize Firebase
var firebaseConfig = {
  apiKey: "AIzaSyAJZgToV46coyP8ZXHlUqCdBBerxPV8t54",
  authDomain: "otp-verifcation-74fcf.firebaseapp.com",
  projectId: "otp-verifcation-74fcf",
  storageBucket: "otp-verifcation-74fcf.appspot.com",
  messagingSenderId: "1092119862329",
  appId: "1:1092119862329:web:7d2ea83d7abb03174701e8"
};
firebase.initializeApp(firebaseConfig);

// Function to send OTP
function sendOTP() {
    var phoneNumber = document.getElementById("phoneNumber").value;
    var appVerifier = new firebase.auth.RecaptchaVerifier('sendOTP', {
      'size': 'invisible'
    });
    firebase.auth().signInWithPhoneNumber(phoneNumber, appVerifier)
        .then((confirmationResult) => {
            window.confirmationResult = confirmationResult;
            document.getElementById("message").innerText = "OTP sent successfully!";
        }).catch((error) => {
            console.error("Error sending OTP:", error);
            document.getElementById("message").innerText = "Error sending OTP: " + error.message;
        });
}

// Function to verify OTP
function verifyOTP() {
    var otp = document.getElementById("otp").value;
    confirmationResult.confirm(otp).then((result) => {
        document.getElementById("message").innerText = "OTP verified successfully!";
    }).catch((error) => {
        console.error("Error verifying OTP:", error);
        document.getElementById("message").innerText = "Error verifying OTP: " + error.message;
    });
}
