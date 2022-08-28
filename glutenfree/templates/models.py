from glutenfree import db

class Starter(db.Model):
    # for starters
    id = db.Column(db.Integer, primary_key=True)
    starter_names=db.Column(db.Text, unique=true, nullable=false)
    starter_tools=db.Column(db.Text, unique=true, nullable=false)
    starter_ingredients=db.Column(db.Text, unique=true, nullable=false)
    starter_directions=db.Column(db.Text, unique=true, nullable=false)


    def __repr__(self):
        return f"Mains('{self.id}', '{self.starter_name}', \
            '{self.starter_tools}')", '{self.starter_ingredients}' \
                '{self.starter_directions}'



class Main(db.Model):
    # for Main Coursers
    id = db.Column(db.Integer, primary_key=True)
    main_names=db.Column(db.Text, unique=true, nullable=false)
    main_tools=db.column(db.Text, unique=true, nullable=false)
    main_ingredients=db.Column(db.Text, unique=true, nullable=false)
    main_directions=db.Column(db.Text, unique=true, nullable=false)

    def __repr__(self):
        return f"Mains('{self.id}', '{self.main_name}', \
            '{self.main_tools}')", '{self.main_ingredients}' \
                '{self.main_directions}'

