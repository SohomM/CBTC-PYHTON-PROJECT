{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "dc50c199",
   "metadata": {},
   "source": [
    "# importing sounddevice and wavio models"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9949e476",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'sounddevice'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01msounddevice\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01msd\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mwavio\u001b[39;00m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;66;03m# Function to record audio\u001b[39;00m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'sounddevice'"
     ]
    }
   ],
   "source": [
    "import sounddevice as sd\n",
    "import wavio\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5e3f1f4b",
   "metadata": {},
   "source": [
    "# code body"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d048cb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def record_audio(duration, filename):\n",
    "    print(\"Recording...\")\n",
    "    \n",
    "    sample_rate = 44100\n",
    "    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')\n",
    "    sd.wait()\n",
    "\n",
    "    # Save the recording to a WAV file\n",
    "    wavio.write(filename, recording, sample_rate, sampwidth=2)\n",
    "\n",
    "    print(f\"Recording saved as {filename}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    \n",
    "    duration = 5  # Change this to adjust the duration of the recording\n",
    "    filename = \"recorded_audio.wav\" \n",
    "\n",
    "    # Calling record audio\n",
    "    record_audio(duration, filename)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
