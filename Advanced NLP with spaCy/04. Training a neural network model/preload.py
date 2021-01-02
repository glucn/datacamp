TEXTS = ['How to preorder the iPhone X',
         'iPhone X is coming',
         'Should I pay $1,000 for the iPhone X?',
         'The iPhone 8 reviews are here',
         'Your iPhone goes up to 11 today',
         'I need a new phone! Any tips?']

TRAINING_DATA = [('How to preorder the iPhone X', {'entities': [(20, 28, 'GADGET')]}),
                 ('iPhone X is coming', {'entities': [(0, 8, 'GADGET')]}),
                 ('Should I pay $1,000 for the iPhone X?', {'entities': [(28, 36, 'GADGET')]}),
                 ('The iPhone 8 reviews are here', {'entities': [(4, 12, 'GADGET')]}),
                 ('Your iPhone goes up to 11 today', {'entities': [(5, 11, 'GADGET')]}),
                 ('I need a new phone! Any tips?', {'entities': []})]

TEST_DATA = ['Apple is slowing down the iPhone 8 and iPhone X - how to stop it',
             "I finally understand what the iPhone X 'notch' is for",
             'Everything you need to know about the Samsung Galaxy S9',
             'Looking to compare iPad models? Here’s how the 2018 lineup stacks up',
             'The iPhone 8 and iPhone 8 Plus are smartphones designed, developed, and marketed by Apple',
             'what is the cheapest ipad, especially ipad pro???',
             'Samsung Galaxy is a series of mobile computing devices designed, manufactured and marketed by Samsung Electronics']
