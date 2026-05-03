its a system that saves states of data so that when a client asks for something again the website wont have to send everything again.

התוכנה יודעת אם למשהו יש cache זמין בכך שהיא מייצרת cache key שמורכב מכל מיני אלמנטים ב request. אם זה תואם, אז הוא מחזיר את העותק. אפשר לייצר עותק מזוייף של cache עם קוד זדוני אבל שיתאים לאותו key.

ישנם כללים למה נשמר בcache ומתי, כל אתר והכללים שלו. robots.txt כמעט תמיד ישמר, כי הוא לרוב לא משתנה.

ממה שאני מבין, אתה שולח url שלך למישהו, המשתמש מזין פרטים מסויימים, ואתה אחר כך לוקח חזרה את המידע ויכול לצפות בו? לא מאוד הבנתי עד כה. בוא נראה מה עוד אלמד.