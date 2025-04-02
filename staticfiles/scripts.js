document.addEventListener("DOMContentLoaded", function () {
    const uploadForm = document.getElementById("upload-form");
    const fileInput = document.getElementById("image-input");
    const previewImage = document.getElementById("image-preview");
    const messageBox = document.getElementById("message-box");

    // Allowed file types and max size (5MB)
    const allowedExtensions = ["jpg", "jpeg", "png"];
    const maxFileSize = 5 * 1024 * 1024;

    // Function to display messages
    function showMessage(type, text) {
        messageBox.innerHTML = `<div class="${type}">${text}</div>`;
        setTimeout(() => {
            messageBox.innerHTML = "";
        }, 4000);
    }

    // Live preview of the selected image
    fileInput.addEventListener("change", function () {
        const file = this.files[0];
        if (file) {
            const fileExtension = file.name.split(".").pop().toLowerCase();

            if (!allowedExtensions.includes(fileExtension)) {
                showMessage("error", "Invalid file format! Only JPG, JPEG, and PNG are allowed.");
                fileInput.value = "";
                return;
            }

            if (file.size > maxFileSize) {
                showMessage("error", "File is too large! Max size is 5MB.");
                fileInput.value = "";
                return;
            }

            const reader = new FileReader();
            reader.onload = function (e) {
                previewImage.src = e.target.result;
                previewImage.style.display = "block";
            };
            reader.readAsDataURL(file);
        } else {
            previewImage.style.display = "none";
        }
    });

    // Form submission with validation
    uploadForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const file = fileInput.files[0];
        if (!file) {
            showMessage("error", "Please select an image to upload.");
            return;
        }

        // Show a loading message
        showMessage("loading", "Uploading image...");

        // Submit the form
        this.submit();
    });
});
