Feature: Basic Requests for automationintesting API
    As a user I want to be able to test automation in testing API.

    @TC-2 @api
    Scenario: The user can get a ping re API Endpoint 
        When the client requests the ping endpoint
        Then the request will return "201" status code
        

    @TC-3 @api
    Scenario Outline: The user can get get a booking from an <id> 
        Given the client is authenticated
        When the client requests "<endpoint>" for id "<id>"
        Then the request will return "200" status code
        Then the request will return "<firstname>" firstname
    
    Examples: 
        | endpoint | id    | firstname   |
        | booking  | 81305 | NAME_644453 |
        | booking  | 79811 | KAM9XK7JN   |

