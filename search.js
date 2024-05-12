const profileSuggestions = {
    "Customer": ["894531069061266030", "1969421b 18442190813b", "6018609623462647744", "4432388076718555246", "17505316106326511065", "6150681532737613937", "17715906626570615896", "17842630370067135567", "10574848487411271014"]
};


function showSuggestions() {
    const input = document.getElementById("searchInput").value.toLowerCase();
    const profileSuggestionsDiv = document.getElementById("profileSuggestions");
    profileSuggestionsDiv.innerHTML = "";

    Object.values(profileSuggestions).forEach(suggestions => {
        suggestions.forEach(profile => {
            if (profile.toLowerCase().includes(input)) {
                const suggestion = document.createElement("div");
                suggestion.textContent = profile;
                suggestion.className = "profile-suggestion";
                suggestion.onclick = () => {
                    document.getElementById("searchInput").value = profile;
                    profileSuggestionsDiv.style.display = "none";
                };
                profileSuggestionsDiv.appendChild(suggestion);
            }
        });
    });

    profileSuggestionsDiv.style.display = profileSuggestionsDiv.children.length > 0 ? "block" : "none";
}

function navigateToProfile(profileName) {
    if (profileName === "894531069061266030" || profileName === "10743516050352051975") {
        window.location.href = "profile6.html";
    } else if (profileName === "1969421b 18442190813b" || profileName === "362966b18442341453b") {
        window.location.href = "profile1.html";
    } else if (profileName === "6018609623462647744" || profileName === "7813136397831853268") {
        window.location.href = "profile4.html";
    } else if (profileName === "4432388076718555246" || profileName === "1618828947225592661") {
        window.location.href = "profile5.html";
    } else if (profileName === "17505316106326511065" || profileName === "7986011032199863210") {
        window.location.href = "profile7.html";
    } else if (profileName === "6150681532737613937" || profileName === "7711083807467252250") {
        window.location.href = "profile8.html";
    } else if (profileName === "17715906626570615896" || profileName === "118114411501563384908") {
        window.location.href = "profile9.html";
    } else if (profileName === "17842630370067135567" || profileName === "16261514606242392388") {
        window.location.href = "profile10.html";
    }
}



function search() {
    const searchInput = document.getElementById("searchInput").value;
    
    console.log("Searching for:", searchInput);
    navigateToProfile(searchInput); // Navigate to profile page if search input matches profile suggestion
}


function closeSuggestions() {
    document.getElementById("profileSuggestions").style.display = "none";
}


document.getElementById("searchInput").addEventListener("input", function(event) {
    showSuggestions();
    
    
    if (!this.value.trim()) {
        closeSuggestions();
    }
});


document.addEventListener("click", function(event) {
    const profileSuggestionsDiv = document.getElementById("profileSuggestions");
    const searchInput = document.getElementById("searchInput");
    if (!searchInput.contains(event.target) && !profileSuggestionsDiv.contains(event.target)) {
        closeSuggestions();
    }
});


document.querySelector(".search-btn").addEventListener("click", function(event) {
    search();
});
