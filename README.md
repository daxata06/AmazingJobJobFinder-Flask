GastarbaiterLux (ГастарбайтерЛюкс) job finder
pet-project

Stack: Flask, Sqlalchemy, Postgresql

About:
The website for job searching, includes 2 modes for register: applicant mpd; employer mod.
Modules:
-Registration
For applicants and employers
Registration for applicants includes such fields as: name, surname, email, password, profession.
Registration for employers includes such fields as: name, surname, company name, profession looking for.
-Auth
Provides for employers and applicants together in one view. Has the fields as email and password.
-Profile 
For applicants:
In profile view applicants can do usually things as edit/add information to their profiles:
 -Set/Change/Delete photo
 -Set/Change additional profile information 
Also applicants can approve or reject invites from employers & check their profiles
For employers:
In own profiles employers can check information about their invites for applicants (possibility to see the invite status)

-Main page of the website
On the main page depending of the user status provides: auth/register (if user is not authorized), link to profile view (if user is authorized). Also for both groups: link to search view. 

When any users open the main page they can to see 5 cards of random applicants. Any user can open any profile of any user and check their information

Employers plays the key role on the website. They selecting applicants and invites their uses the special button (invite the applicant, пригласить соискателя). After this applicant can make a desigion uses two buttons (approve/reject). After this, employer will see the user`s desigion on his profile page.

Following the link below, you can see the video provides how to the website works.
