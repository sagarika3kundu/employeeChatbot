<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/rasa-starter-pack/704 --> 

## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot


## intent:name
- My name is [Juste](name)  <!--- Square brackets contain the value of entity while the text in parentheses is a a label of the entity --> 
- hi, i am [ABc](name)
- hello, i'm [dgf](name)
- I am [Josh](name)
- I'm [Lucy](name)
- People call me [Greg](name)
- It's [David](name)
- Usually people call me [Amy](name)
- My name is [John](name)
- You can call me [Sam](name)
- Please call me [Linda](name)
- Name name is [Tom](name)
- I am [Richard](name)
- I'm [Tracy](name)
- Call me [Sally](name)
- I am [Philipp](name)
- I am [Charlie](name)


## intent:MRI_update_sheet
- the region is [International](region) and related to [IMR/EPIC](rel)
- [Canada](region)
- [IMR](rel)
- [US/AU/NZ/JAPAC](region) [GRIP](rel)
- [All](region) and [Box](rel)
- the region is [International](region) and related to [IMR/EPIC](rel)
- It is [Canada](region)
- it is [IMR](rel)
- they are [US/AU/NZ/JAPAC](region) [GRIP](rel)
- [All](region) and [Box](rel)
- the region is [International](region) and related to [IMR/EPIC](rel)
- for [Global](region)
- for [IMR](rel)
- regarding [US/AU/NZ/JAPAC](region) [GRIP](rel)
- [All](region) and [Box](rel)
- the region is [International](region) and related to [IMR/EPIC](rel)
- [Canada](region)
- [IMR](rel)
- [US/AU/NZ/JAPAC](region) [GRIP](rel)
- [All](region) and [Box](rel)
- [AU-NZ](region)
- [la](region)


## lookup:region
C:\Users\Laptop\Desktop\demo\data\lookup_tables\region.txt

## lookup:rel
C:\Users\Laptop\Desktop\demo\data\lookup_tables\rel.txt

## intent:thanks
- Thanks
- Thank you
- Thank you so much
- Thanks bot
- Thanks for that
- cheers
- cheers bro
- ok thanks!
- perfect thank you
- thanks a bunch for everything
- thanks for the help
- thanks a lot
- amazing, thanks
- cool, thanks
- cool thank you


## intent:affirm
- yes
- yes sure
- absolutely
- for sure
- yes yes yes
- definitely


## intent:goodbye <!--- The label of the intent --> 
- Bye 			<!--- Training examples for intent 'bye'--> 
- Goodbye
- See you later
- Bye bot
- Goodbye friend
- bye
- bye for now
- catch you later
- gotta go
- See you
- goodnight
- have a nice day
- i'm off
- see you later alligator
- we'll speak soon