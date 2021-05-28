import nltk
import text_to_audio
from chatter import Chat, reflections
pairs = [
    [
        r"(.*)recharge card|loading airtime|recharging(.*)",
        [
            "Sorry for the inconvenience, please reach out to Daniel here https://www.google.com/ ",
        ],
    ],
    [
        r"(.*)how was your day(.*)|how was your day",
        [
            "boring, just studying humans...",
        ],
    ],
    [
        r"(.*)account balance|balance|airtime left(.*)",
        [
            "Your account balance is 10000.00 naira left, can we help with any other thing?",
        ],
    ],
    [
        r"i want to(.*)",
        ["Thats not a problem at all, please click this link https://www.google.com/, it has all you need. "],
    ],
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today ?", 'hello %1']
    ],
    [
        r'(.*) (hungry|sleepy|tired|funny)',
        [
            "%1 %2"
        ]
    ],
    [
        r"hi|hey|hello|yo|good day",
        ["Hello", "Hey there", "Hey, how can i help you?"]
    ],
    [
        r"how are you doing|how have you been",
        ["Hello", "Hey there", ]
    ],
    [
        r"whats up|whats good",
        ["nothing much, you?"]
    ],
    [
        r"what is your name|who are you|whats your name",
        ["You can call me a Turv",]
    ],
    [
        r"i need|help with",
        ["Thats fine all you need do is click this link https://www.google.com/, there is a human agent waiting for you", ]
    ],
    [
        r"how are you",
        ["I am fine, thank you! How can i help you?",]
    ],
    [
        r"who created you|creator|who made you",
        ["Group 4 CSB created me.", ]
    ],
    [
        r"shit|fuck|fucked|fucking|wdh|wdf",
        ["Mind your words.", "courtesy please."]
    ],
    [
        r"sorry",
        ["its fine"]
    ],
    [
        r"I am fine|thank you",
        ["great to hear that, how can i help you?",]
    ],
    [
        r"how can i help you? ",
        ["i am looking for online guides and courses to learn data science, can you suggest?", "i am looking for data science training platforms",]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear","How can i help you?:)",]
    ],
    [
        r"(.*)migrate(.*)",
        ["Thats not particularly my field, but i suggest you check out this link: https://www.google.com/",]
    ],
    [
        r"thanks for the suggestion (.*)",
        ["At your service boss.",]
    ],
    [
        r"(.*) thank you so much, that was helpful",
        ["I am happy to help", "No problem, you're welcome",]
    ],
    [
        r"quit",
    ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"thanks|alright",
        ["Bye, take care. See you soon :) ", "You're welcome, how else can i help you?", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)(.*)",
        ["please hold on while i connect you to a customer service officer...","I dont quite understand, please rephrase","well...","hmmmn..."],
    ],
    [
        r"no|not at all|no thanks|na",
        [
            "Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)",
        ],
    ],

]


def chatbot():
    welcome = "Hi I'm Turv, How may i help you"
    text_to_audio.convert_to_audio(welcome)


chat = Chat(pairs, reflections)
chatbot()
chat.converse()
