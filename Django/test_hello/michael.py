
class Skill():
    
    def __init__( self, name, age, city, state, country, language ):

        self.name = name
        self.age = age
        self.city = city
        self.state = state
        self.country = country
        self.language = language

    def description( self ):
        return "%s, %d age, live-in city %s in state - %s, experienced with %s" %(self.name, self.age, self.city, self.state, self.country)

    def list_skills( self ):

        string_out = ""
        for i in self.language:
            string_out += i + "\n"

        return string_out

list_skills = ["Python","Java","JS","R","NodeJs","Django","SQLite","Postgresql","MongoDB","MEMES"]
michael = Skill("Michael", 23, "Guarabira", "PB", "Brazil", list_skills)

print(michael.description())