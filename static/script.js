// =====================================
// BACKEND API URL
// =====================================

const API_URL = "https://myproject.onrender.com";

// =====================================
// HELPER FUNCTION FOR API RESPONSE
// =====================================

async function getResponseData(response) {

    const data = await response.json();

    if (!response.ok) {
        throw new Error(
            typeof data.detail === "string"
                ? data.detail
                : JSON.stringify(data.detail || data)
        );
    }

    return data;
}


// =====================================
// 1. USER REGISTRATION
// =====================================

document.getElementById("registerForm").addEventListener(
    "submit", async function(event) {

    event.preventDefault();

    const full_name = document.getElementById("regUsername").value;
    const email = document.getElementById("regEmail").value;
    const password = document.getElementById("regPassword").value;

    try {

        const response = await fetch(`${API_URL}/register`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                full_name: full_name,
                email: email,
                password: password

            })

        });

        const data = await getResponseData(response);

        document.getElementById("registerMessage").innerText =
            "Registration Successful!";

        console.log("Registration Response:", data);

        document.getElementById("registerForm").reset();

    }

    catch(error) {

        document.getElementById("registerMessage").innerText =
            error.message;

        console.error("Registration Error:", error);

    }

});


// =====================================
// 2. USER LOGIN
// =====================================

document.getElementById("loginForm").addEventListener(
    "submit", async function(event) {

    event.preventDefault();

    const email = document.getElementById("loginEmail").value;
    const password = document.getElementById("loginPassword").value;

    try {

        const response = await fetch(`${API_URL}/login`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                email: email,
                password: password

            })

        });

        const data = await getResponseData(response);

        // Store JWT Token

        localStorage.setItem("access_token", data.token);

        document.getElementById("loginMessage").innerText =
            "Login Successful!";

        console.log("Login Response:", data);

        document.getElementById("loginForm").reset();

    }

    catch(error) {

        document.getElementById("loginMessage").innerText =
            error.message;

        console.error("Login Error:", error);

    }

});


// =====================================
// 3. GET USER PROFILE
// =====================================

async function getProfile() {

    const token = localStorage.getItem("access_token");

    if (!token) {

        alert("Please login first!");

        return;

    }

    try {

        const response = await fetch(`${API_URL}/profile`, {

            method: "GET",

            headers: {

                "Authorization": `Bearer ${token}`

            }

        });

        const data = await getResponseData(response);

        document.getElementById("result").innerText =
            JSON.stringify(data, null, 2);

        console.log("Profile:", data);

    }

    catch(error) {

        document.getElementById("result").innerText =
            error.message;

        console.error("Profile Error:", error);

    }

}


// =====================================
// 4. USER LOGOUT
// =====================================

function logout() {

    localStorage.removeItem("access_token");

    document.getElementById("loginMessage").innerText =
        "Logged out successfully!";

    document.getElementById("result").innerText = "";

    alert("Logout Successful!");

}