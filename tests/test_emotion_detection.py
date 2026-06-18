import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector (unittest.TestCase):

    def test_dominant_emotions(self):

        test_cases = [
            {"text": "I am glad this happened", "expected": "joy"},
            {"text": "I am really mad about this", "expected": "anger"},
            {"text": "I feel disgusted just hearing about this", "expected": "disgust"},
            {"text": "I am so sad about this", "expected": "sadness"},
            {"text": "I am really afraid that this will happen", "expected": "fear"}
        ]

        for case in test_cases:
            with self.subTest(statement=case["text"]):
                result = emotion_detector(case["text"])

                self.assertIsInstance(result,dict)
                self.assertIn('dominant_emotion', result, f"Missing 'dominant_emotion' for text: {case['text']}")


                actual_emotion = result['dominant_emotion']
                self.assertEqual(
                    actual_emotion, 
                    case["expected"], 
                    f"Expected '{case['expected']}' but got '{actual_emotion}' for statement: '{case['text']}'"
                )
if __name__ == '__main__':
    unittest.main()

