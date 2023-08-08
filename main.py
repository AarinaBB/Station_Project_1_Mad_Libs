import random


# Function to get user input for a specific word
def get_word (prompt):
    return input(f"Enter {prompt}: ")


# Template 1
template1 = (
    f"It was about {get_word('a number')} {get_word('a measure of time')} ago when I arrived at the hospital "
    f"in a {get_word('mode of transportation')}. The hospital is a/an {get_word('adjective')} place, there are a lot of "
    f"{get_word('adjective')} {get_word('noun')} here. There are nurses here who have {get_word('color')} "
    f"{get_word('part of the body')}. If someone wants to come into my room I told them that they have to "
    f"{get_word('verb')} first. I’ve decorated my room with {get_word('a number')} {get_word('noun')}. Today I talked "
    f"to a doctor and they were wearing a {get_word('noun')} on their {get_word('part of the body')}. I heard that "
    f"all doctors {get_word('verb')} {get_word('noun')} every day for breakfast. The most {get_word('adjective')} "
    f"thing about being in the hospital is the {get_word('silly word')} {get_word('noun')}!"
)

# Template 2
template2 = (
    f"This weekend I am going camping with {get_word('a proper noun (person’s name)')}. I packed my lantern, "
    f"sleeping bag, and {get_word('noun')}. I am so {get_word('adjective (feeling)')} to {get_word('verb')} in a tent. "
    f"I am {get_word('adjective (feeling)')} we might see a(n) {get_word('animal')}, I hear they’re kind of dangerous. "
    f"While we’re camping, we are going to hike, fish, and {get_word('verb')}. I have heard that the {get_word('color')} "
    f"lake is great for {get_word('verb (ending in ing)')}. Then we will {get_word('adverb (ending in ly)')} hike "
    f"through the forest for {get_word('a number')} {get_word('measure of time')}. If I see a {get_word('color')} "
    f"{get_word('animal')} while hiking, I am going to bring it home as a pet! At night we will tell "
    f"{get_word('a number')} {get_word('silly word')} stories and roast {get_word('noun')} around the campfire!!"
)

# Template 3
template3 = (
    f"Dear {get_word('a proper noun (person’s name)')}, I am writing to you from a {get_word('adjective')} castle in "
    f"an enchanted forest. I found myself here one day after going for a ride on a {get_word('color')} {get_word('animal')} "
    f"in {get_word('place')}. There are {get_word('adjective')} {get_word('magical creature (plural)')} and "
    f"{get_word('adjective')} {get_word('magical creature (plural)')} here! In the {get_word('room in a house')} "
    f"there is a pool full of {get_word('noun')}. I fall asleep each night on a {get_word('noun')} of "
    f"{get_word('noun (plural)')} and dream of {get_word('adjective')} {get_word('noun (plural)')}. It feels as though "
    f"I have lived here for {get_word('a number')} {get_word('measure of time')}. I hope one day you can visit, "
    f"although the only way to get here now is {get_word('verb (ending in ing)')} on a {get_word('adjective')} "
    f"{get_word('noun')}!!"
)


# Main program
def main ():
    print("Choose a template:")
    print("1. Template 1")
    print("2. Template 2")
    print("3. Template 3")

    choice = input("Enter the number of the template you want to use: ")

    if choice == '1':
        story = template1
    elif choice == '2':
        story = template2
    elif choice == '3':
        story = template3
    else:
        print("Invalid choice.")
        return

    genet_story = story.format(
        adjective=get_word("an adjective"),
        adjective2=get_word("another adjective"),
        adjective3=get_word("yet another adjective"),
        adjective4=get_word("one more adjective"),
        adjective5=get_word("one final adjective"),
        adverb=get_word("an adverb"),
        animal=get_word("an animal"),
        color=get_word("a color"),
        measure_of_time=get_word("a measure of time"),
        mode_of_transportation=get_word("a mode of transportation"),
        noun=get_word("a noun"),
        noun2=get_word("another noun"),
        noun3=get_word("yet another noun"),
        noun4=get_word("one more noun"),
        noun5=get_word("one final noun"),
        part_of_the_body=get_word("a part of the body"),
        part_of_the_body2=get_word("another part of the body"),
        person_name=get_word("a person's name"),
        place=get_word("a place"),
        silly_word=get_word("a silly word"),
        verb=get_word("a verb"),
        verb2=get_word("another verb"),
    )

    print("\nGenerated Story:")
    print(genet_story)


if __name__ == "__main__":
    main()
