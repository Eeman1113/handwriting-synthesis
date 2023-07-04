import numpy as np
from handwriting_synthesis import Hand

all_star = """Somebody once told me the world is gonna roll me
I ain't the sharpest tool in the shed
She was looking kind of dumb with her finger and her thumb
In the shape of an "L" on her forehead"""

s ='''
Once upon a time, in a world where the boundaries between heaven
and earth blurred, there lived a renowned warrior named Sourav Dutta. 
Sourav was known far and wide for his exceptional strength, unmatched 
skills, and unwavering determination. With his chiseled physique and 
piercing eyes, he was often referred to as the "Absolute Chad" by his admirers.

In the celestial realms, there existed a fearsome Demon of heaven known
as Aman. Aman took the form of a mighty dragon with scales as blue as the 
sky and flames that burned with an otherworldly intensity. He had terrorized
the heavenly creatures for centuries, bringing chaos and despair wherever he flew.
The heavenly beings, desperate for a savior, turned their hopes towards Sourav Dutta.

Word of the demon's tyranny reached Sourav's ears, and he felt an intense call to action.
He knew that defeating Aman would be no easy feat, but Sourav was not one to back down from
a challenge. He embarked on a perilous journey, gathering his weapons and honing his skills
along the way.

Guided by a celestial spirit, Sourav made his way to the celestial realms. The heavenly 
beings, in awe of his presence, greeted him with reverence. They recounted tales of the 
devastation caused by Aman and begged Sourav to save them from their eternal torment.

With a resolute heart and unwavering determination, Sourav marched towards the lair
of the mighty dragon. As he approached, the sky darkened, and the ground trembled beneath 
his feet. Aman sensed the arrival of his challenger and unleashed his fiery wrath upon Sourav.

Undeterred, Sourav swiftly dodged the scorching blue flames, his agility and reflexes 
unparalleled. With his sword drawn, he lunged towards the dragon, striking with precision 
and strength. The clash between the Absolute Chad and the Demon of heaven shook the celestial 
realms, a battle of epic proportions.

Aman, with his immense power, fought back fiercely. He unleashed gusts of wind and torrents 
of fire, but Sourav's determination never wavered. He skillfully maneuvered through the chaos, 
evading every attack. With each strike of his sword, Sourav chipped away at the dragon's defenses.

The battle raged on, and it seemed as though victory might elude Sourav. But in a moment of sheer 
willpower, he tapped into a hidden reserve of strength. His muscles bulged, and an indomitable aura 
surrounded him. With an earth-shattering roar, Sourav delivered a final, devastating blow to Aman, 
piercing through the dragon's heart.

As the demon fell, a collective gasp of relief echoed through the celestial realms. The heavenly 
beings rejoiced, their savior victorious. Sourav Dutta had slain the Demon of heaven, liberating 
the realm from his reign of terror.

From that day forward, Sourav's name was etched in the annals of celestial history. He became a 
legend, a symbol of bravery and heroism. The heavenly beings revered him as their protector, and 
his story echoed through generations, inspiring others to rise against adversity.

Sourav Dutta, the Absolute Chad, had conquered the heavens, proving that with unwavering 
determination, even the mightiest of demons could be vanquished.'''

downtown = """Making my way downtown
Walking fast
Faces pass
And I'm home-bound"""

give_up = """Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you"""

lines = [
    "Father time, I'm running late",
    "I'm winding down, I'm growing tired",
    "Seconds drift into the night",
    "The clock just ticks till my time expires",
]

if __name__ == '__main__':
    hand = Hand()

    # usage demo
    biases = [.75 for i in lines]
    styles = [9 for i in lines]
    stroke_colors = ['red', 'green', 'black', 'blue']
    stroke_widths = [1, 2, 1, 2]

    hand.write(
        filename='img/usage_demo.svg',
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_colors=stroke_colors,
        stroke_widths=stroke_widths
    )

    # demo number 1 - fixed bias, fixed style
    lines = s.split("\n")
    biases = [.75 for i in lines]
    styles = [12 for i in lines]

    hand.write(
        filename='img/all_star.svg',
        lines=lines,
        biases=biases,
        styles=styles,
    )

    # demo number 2 - fixed bias, varying style
    lines = downtown.split("\n")
    biases = [.75 for i in lines]
    styles = np.cumsum(np.array([len(i) for i in lines]) == 0).astype(int)

    hand.write(
        filename='img/downtown.svg',
        lines=lines,
        biases=biases,
        styles=styles,
    )

    # demo number 3 - varying bias, fixed style
    lines = give_up.split("\n")
    biases = .2 * np.flip(np.cumsum([len(i) == 0 for i in lines]), 0)
    styles = [7 for i in lines]

    hand.write(
        filename='img/give_up.svg',
        lines=lines,
        biases=biases,
        styles=styles,
    )
