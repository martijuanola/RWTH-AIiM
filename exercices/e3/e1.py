import librosa
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # load file
    filepath = "data/classical.mp3"
    y, sr = librosa.load(filepath)

    # get onsets and their times
    onsets = librosa.onset.onset_detect(y=y, sr=sr)
    onset_times = librosa.frames_to_time(onsets, sr=sr)
    print(onset_times)

    # plot everything
    plt.figure()
    ax = plt.subplot(1, 1, 1)
    ax.set_facecolor("#333333")

    librosa.display.waveshow(y, sr=sr, ax=ax, alpha=0.8)

    ax.vlines(onset_times, -1, 1, linestyle="-", alpha=0.05, color="yellow")
    ax.set_xlabel("time in seconds")
    ax.set_ylabel("amplitude")

    plt.show()
