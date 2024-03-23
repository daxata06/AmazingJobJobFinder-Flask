<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>GastarbaiterLux (ГастарбайтерЛюкс) Job Finder</h1>
<h2>pet-project</h2>

<h3>Stack:</h3>
<p>Flask, Sqlalchemy, Postgresql</p>

<h3>About:</h3>
<p>
    The website for job searching, includes 2 modes for register: applicant mode; employer mode.
</p>

<h3>Modules:</h3>
<ul>
    <li>
        <h4>Registration</h4>
        <p>
            For applicants and employers.
            <br>Registration for applicants includes such fields as: name, surname, email, password, profession.
            <br>Registration for employers includes such fields as: name, surname, company name, profession looking for.
        </p>
    </li>
    <li>
        <h4>Auth</h4>
        <p>
            Provides for employers and applicants together in one view. Has the fields as email and password.
        </p>
    </li>
    <li>
        <h4>Profile</h4>
        <p>
            For applicants:
            <br>In profile view applicants can do usually things as edit/add information to their profiles:
            <ul>
                <li>Set/Change/Delete photo</li>
                <li>Set/Change additional profile information</li>
            </ul>
            Also applicants can approve or reject invites from employers & check their profiles.
            <br>For employers:
            <br>In own profiles employers can check information about their invites for applicants (possibility to see the invite status).
        </p>
    </li>
    <li>
        <h4>Main page of the website</h4>
        <p>
            On the main page depending of the user status provides: auth/register (if user is not authorized), link to profile view (if user is authorized). Also for both groups: link to search view.
            <br>When any users open the main page they can to see 5 cards of random applicants. Any user can open any profile of any user and check their information.
            <br>Employers plays the key role on the website. They selecting applicants and invites their uses the special button (invite the applicant, пригласить соискателя). After this applicant can make a desigion uses two buttons (approve/reject). After this, employer will see the user`s desigion on his profile page.
        </p>
    </li>
</ul>

<p>Following the link below, you can see the video demonstrates how the website works.</p>

</body>
</html>
