@kissflow
Feature: Trello Cards Validations

  @validatecardfuctionality
  Scenario:  Scenario to validate login functionality , Cards Creation, Cards Movement and Cards Re-align
	  Given 	Login into Trello using credentials
	  When  Create a new Board "Project"
	  Then Create "4" Lists with status as "Not Started", "In Progress", "QA", "Done"  respectively
	  And Create "4" Cards. : "Card 1", "Card 2", "Card 3", "Card 4" under the list "Not Started".
	  And Move Card "2" to "In Progress".
	  And Move Card "3" to "QA".
	  And Move Card "2" to "QA".
	  And  Open Card "1" and Assign it to the current logged in user and then leave a comment on Card  saying "I am done"