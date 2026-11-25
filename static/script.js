// ========================================
// API CONFIGURATION
// ========================================

const API_URL = ""; 

// JWT Token
let accessToken = localStorage.getItem("access_token");


// ========================================
// HELPER FUNCTION
// ========================================

async function apiRequest(endpoint, options = {}) {

    const headers = {
        "Content-Type": "application/json",
        ...options.headers
    };

    // Add JWT token if available
    if (accessToken) {
        headers["Authorization"] = `Bearer ${accessToken}`;
    }

    try {

        const response = await fetch(`${API_URL}${endpoint}`, {
            ...options,
            headers
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                typeof data.detail === "string"
                    ? data.detail
                    : JSON.stringify(data.detail || data)
            );
        }

        return data;

    } catch (error) {

        console.error("API Error:", error);

        throw error;
    }
}


// ========================================
// 1. USER REGISTRATION
// ========================================

const registerForm = document.getElementById("registerForm");

registerForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const inputs = registerForm.querySelectorAll("input");

    const full_name = inputs[0].value.trim();
    const email = inputs[1].value.trim();
    const password = inputs[2].value;

    const message = document.getElementById("registerMessage");

    try {

        message.innerText = "Registering...";

        const data = await apiRequest("/register", {

            method: "POST",

            body: JSON.stringify({
                full_name: full_name,
                email: email,
                password: password
            })

        });

        message.innerText = "Registration Successful!";

        registerForm.reset();

        console.log("Registered User:", data);

    } catch (error) {

        message.innerText = error.message;

    }

});


// ========================================
// 2. USER LOGIN
// ========================================

const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const email = document.getElementById("loginEmail").value.trim();

    const password = document.getElementById("loginPassword").value;

    const message = document.getElementById("loginMessage");

    try {

        message.innerText = "Logging in...";

        const data = await apiRequest("/login", {

            method: "POST",

            body: JSON.stringify({
                email: email,
                password: password
            })

        });

        // Save JWT Token
        accessToken = data.token;

        localStorage.setItem("access_token", accessToken);

        message.innerText = "Login Successful!";

        loginForm.reset();

        console.log("Login Response:", data);

    } catch (error) {

        message.innerText = error.message;

    }

});


// ========================================
// 3. GET USER PROFILE
// ========================================

async function getProfile() {

    const result = document.getElementById("result");

    try {

        result.innerText = "Loading Profile...";

        if (!accessToken) {
            throw new Error("Please login first!");
        }

        const data = await apiRequest("/profile", {

            method: "GET"

        });

        result.innerText = JSON.stringify(data, null, 2);

        console.log("User Profile:", data);

    } catch (error) {

        result.innerText = error.message;

    }

}


// ========================================
// 4. GET ALL USERS
// ========================================

async function getUsers() {

    const result = document.getElementById("result");

    try {

        result.innerText = "Loading Users...";

        if (!accessToken) {
            throw new Error("Please login first!");
        }

        const data = await apiRequest("/users", {

            method: "GET"

        });

        result.innerText = JSON.stringify(data, null, 2);

        console.log("All Users:", data);

    } catch (error) {

        result.innerText = error.message;

    }

}


// ========================================
// 5. USER LOGOUT
// ========================================

function logout() {

    accessToken = null;

    localStorage.removeItem("access_token");

    document.getElementById("result").innerText =
        "Logged out successfully!";

    document.getElementById("loginMessage").innerText =
        "You are logged out.";

    console.log("User Logged Out");

}


// ========================================
// END OF SCRIPT
// ========================================