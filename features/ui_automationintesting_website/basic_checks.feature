Feature: I want to Test automationintesting Website
    As a user I want to be able browse automation in testing website.

    @TC-1 @web_ui
    Scenario: The User wants to summit a enquiry to automationintesting Website 
        When the user navigates to "https://automationintesting.online/"
        Then the browser title is "Restful-booker-platform demo"
        Then the url is "https://automationintesting.online/"
        Then the h2 title is "Rooms"
        When the user inputs Name "Test User1"
        When the user inputs Email "Testuser1@fakeemail.comm"
        When the user inputs Phone "01234567890"
        When the user inputs Subject "Test Subject12345"
        When the user inputs Message "Test Message input 1234578910"
        When the user clicks on Submit button
        Then the user should see a h2 message "Thanks for getting in touch Test User1"
