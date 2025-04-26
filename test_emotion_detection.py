import unittest

from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetection(unittest.TestCase):

    def _assert_emotion(self, text, expected_emotion):
        result = emotion_detector(text)["dominant_emotion"]
        self.assertEqual(result, expected_emotion)

    def test_emotion_detector(self):
        self._assert_emotion("I am glad this happened", "joy")
        self._assert_emotion("I am really mad about this", "anger")
        self._assert_emotion("I feel disgusted just hearing about this", "disgust")
        self._assert_emotion("I am so sad about this", "sadness")
        self._assert_emotion("I am really afraid that this will happen", "fear")

if __name__ == '__main__':
    unittest.main()