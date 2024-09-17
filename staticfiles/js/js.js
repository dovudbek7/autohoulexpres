document.querySelectorAll('.phone_number').forEach(function (input) {
    input.addEventListener('input', function (e) {
        var input = e.target.value.replace(/\D/g, ''); // Remove all non-digit characters
        var formattedInput = input;

        if (input.length > 0) {
            formattedInput = '(' + input.substring(0, 3); // Add (XXX
        }
        if (input.length >= 4) {
            formattedInput += ') ' + input.substring(3, 6); // Add (XXX) XXX
        }
        if (input.length >= 7) {
            formattedInput += '-' + input.substring(6, 10); // Add (XXX) XXX-XXXX
        }

        e.target.value = formattedInput;
    });
});
$(document).ready(
    function () {
        $(".log-in").click(
            function () {
                $(".panel_call").animate({ width: 'toggle' }, 350)
                return false;
            }
        )
    }
);
function displayNames(value) {
    input.value = value;
    removeElements();
}

$(".tab").css("display", "none");
$("#tab-1").css("display", "block");

function run(hideTab, showTab) {
    if (hideTab < showTab) {
        var currentTab = $('#tab-' + hideTab);
        var inputs = $(currentTab).find("input, select");
        var isValid = true;

        inputs.each(function () {
            if ($(this).prop('required') && !$(this).val()) {
                $(this).addClass('invalid').removeClass('valid');
                isValid = false;
            } else {
                $(this).addClass('valid').removeClass('invalid');
            }
        });

        if (!isValid) {
            return false;
        }
    }

    $('#model').removeAttr('disabled');
    $('#year').removeAttr('disabled');

    for (let i = 1; i < showTab; i++) {
        $("#step-" + i).css("opacity", "1");
    }

    // Switch tab
    $("#tab-" + hideTab).css("display", "none");
    $("#tab-" + showTab).css("display", "block");
}

$("input, select").on("input change", function () {
    if ($(this).prop('required') && !$(this).val()) {
        $(this).addClass('invalid').removeClass('valid');
    } else {
        $(this).addClass('valid').removeClass('invalid');
    }
});
let locations = [
    "YARBO, AL 36558", "BIRMINGHAM, AL 35201", "MOBILE, AL 36601", "HUNTSVILLE, AL 35801", "MONTGOMERY, AL 36101",
    "ANCHORAGE, AK 99501", "PHOENIX, AZ 85001", "TUCSON, AZ 85701", "MESA, AZ 85201", "SCOTTSDALE, AZ 85250",
    "LITTLE ROCK, AR 72201", "LOS ANGELES, CA 90001", "SAN DIEGO, CA 92101", "SAN FRANCISCO, CA 94101",
    "SACRAMENTO, CA 94203", "DENVER, CO 80201", "BRIDGEPORT, CT 06601", "NEW HAVEN, CT 06501",
    "WILMINGTON, DE 19801", "MIAMI, FL 33101", "ORLANDO, FL 32801", "TALLAHASSEE, FL 32301",
    "ATLANTA, GA 30301", "AUGUSTA, GA 30901", "HONOLULU, HI 96801", "BOISE, ID 83701",
    "CHICAGO, IL 60601", "SPRINGFIELD, IL 62701", "INDIANAPOLIS, IN 46201", "DES MOINES, IA 50301",
    "WICHITA, KS 67201", "LOUISVILLE, KY 40201", "BATON ROUGE, LA 70801", "NEW ORLEANS, LA 70112",
    "PORTLAND, ME 04101", "BALTIMORE, MD 21201", "BOSTON, MA 02101", "DETROIT, MI 48201",
    "MINNEAPOLIS, MN 55401", "JACKSON, MS 39201", "ST. LOUIS, MO 63101", "BILLINGS, MT 59101",
    "OMAHA, NE 68101", "LAS VEGAS, NV 89101", "MANCHESTER, NH 03101", "NEWARK, NJ 07101",
    "ALBUQUERQUE, NM 87101", "NEW YORK, NY 10001", "CHARLOTTE, NC 28201", "FARGO, ND 58102",
    "COLUMBUS, OH 43201", "OKLAHOMA CITY, OK 73101", "PORTLAND, OR 97201", "PHILADELPHIA, PA 19101",
    "PROVIDENCE, RI 02901", "CHARLESTON, SC 29401", "SIOUX FALLS, SD 57101", "NASHVILLE, TN 37201",
    "HOUSTON, TX 77001", "DALLAS, TX 75201", "AUSTIN, TX 73301", "SALT LAKE CITY, UT 84101",
    "BURLINGTON, VT 05401", "RICHMOND, VA 23218", "SEATTLE, WA 98101", "CHARLESTON, WV 25301",
    "MILWAUKEE, WI 53201", "CHEYENNE, WY 82001"
];

// Sort names in ascending order
let sortedNames = locations.sort();

// Set up input elements
let pickupInput = document.getElementById("pickup_input");
let deliveryInput = document.getElementById("delivery_input");

// Event listeners for both inputs
pickupInput.addEventListener("keyup", function () {
    handleInput(this, "pickup_list");
});

deliveryInput.addEventListener("keyup", function () {
    handleInput(this, "delivery_list");
});

// Function to handle input suggestion
function handleInput(inputElement, listId) {
    // Remove existing suggestions
    removeElements(listId);

    // Check if the input is not empty
    if (inputElement.value === "") {
        return;
    }

    // Loop through sorted names
    for (let i of sortedNames) {
        // Convert input to lowercase and compare with each string
        if (i.toLowerCase().startsWith(inputElement.value.toLowerCase())) {
            // Create an li element
            let listItem = document.createElement("li");
            listItem.classList.add("list-items");
            listItem.style.cursor = "pointer";
            listItem.setAttribute("onclick", "displayNames('" + i + "', '" + inputElement.id + "')");

            // Display matched part in bold
            let word = "<b>" + i.substr(0, inputElement.value.length) + "</b>";
            word += i.substr(inputElement.value.length);

            // Set the HTML content of the list item
            listItem.innerHTML = word;

            // Append the list item to the appropriate list
            document.getElementById(listId).appendChild(listItem);
        }
    }
}

// Function to display the selected name in the input field
function displayNames(value, inputId) {
    document.getElementById(inputId).value = value;
    removeElements(inputId === "pickup_input" ? "pickup_list" : "delivery_list");
}

// Function to remove old suggestions
function removeElements(listId) {
    let listElement = document.getElementById(listId);
    while (listElement.firstChild) {
        listElement.removeChild(listElement.firstChild);
    }
}


// swiper
// Params
var sliderSelector = '.swiper-container',
    options = {
      init: false,
      loop: true,
      speed:800,
      slidesPerView: 2, // or 'auto'
      // spaceBetween: 10,
      centeredSlides : true,
      effect: 'coverflow', // 'cube', 'fade', 'coverflow',
      coverflowEffect: {
        rotate: 50, // Slide rotate in degrees
        stretch: 0, // Stretch space between slides (in px)
        depth: 100, // Depth offset in px (slides translate in Z axis)
        modifier: 1, // Effect multipler
        slideShadows : true, // Enables slides shadows
      },
      grabCursor: true,
      parallax: true,
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      breakpoints: {
        1023: {
          slidesPerView: 1,
          spaceBetween: 0
        }
      },
      // Events
      on: {
        imagesReady: function(){
          this.el.classList.remove('loading');
        }
      }
    };
var mySwiper = new Swiper(sliderSelector, options);

// Initialize slider
mySwiper.init();



jQuery(window).on("load", function() {
    $('#preloader').fadeOut(500);
    $('#main-wrapper').addClass('show');
});

