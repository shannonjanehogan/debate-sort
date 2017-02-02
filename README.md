This application is being built for the UBC Debate Society, in order to automate sorting debaters into teams and rooms.

Currently, this application handles British Parliamentary Debate Style.

Features:

- Users can select debate, judge, or debate/judge(indifferent preference).
- Users are sorted into teams of two if debate was selected
- A room is composed of four teams of two and at least one judge
- If there are an odd number of debaters and/or users that have selected debate/judge, the application will check if judges are needed, and if not, will make a half room composed of two teams of two and at least one judge
- If there are too many debaters, but not enough for a new room, the extra debaters become judges

Upcoming Features:

- Allow users to select a partner preference
- Read data in from a csv file
- Output the results to a csv file

Stretch Features:

- Create database and store attendance data
- Match based on skill (aka novice rooms, pro rooms, pro-am rooms)
- Make a web page with a form for debaters to sign up
- Make an app with a form for debaters to sign up
- When the rooms have been sorted, send users a text message with their room number, partner information, and team position

To launch:
- Clone the repository
- Run the command python sort_rooms.py

Contributors:

Shannon Hogan
Grant Bradshaw
Christina Hess