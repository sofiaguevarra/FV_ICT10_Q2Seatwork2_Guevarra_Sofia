from pyscript import display, document
def general_weighted_average(e):
    Science = float(document.getElementById('Science').value)
    Math = float(document.getElementById('Math').value)
    English = float(document.getElementById('English').value)
    Filipino = float(document.getElementById('Filipino').value)
    Social_studies = float(document.getElementById('Social studies').value)
    ICT = float(document.getElementById('ICT').value)
    #this is to get each of the subjects value and when the user clicks the "Calculate GWA" button from the html, this function will be called

    units_subject = (5, 5, 5, 3, 3, 2)
    weighted_sum = (Science * 5 + Math * 5 + English * 5 + Filipino * 3 + Social_studies * 3 + ICT * 2)
    total_units = (5 * 3) + 3 + 3 + 2
    gwa = weighted_sum / total_units
    #this is the actual calculation itself, multiplying each subject unit by the grade then dividing it

    subjects = ['Science','Math','English','Filipino','Social Studies','ICT'] #this is a list
    #              0          1       2          3               4            5
    summary = f"""{subjects[0]}: {Science:.0f}
    {subjects[1]}: {Math:.0f}
    {subjects[2]}: {English:.0f}
    {subjects[3]}: {Filipino:.0f}
    {subjects[4]}: {Social_studies:.0f}
    {subjects[5]}: {ICT:.0f}
        """
    display(f'Name: {first_name} {last_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')
    #the display functions will help us show the summary or the computed grades

