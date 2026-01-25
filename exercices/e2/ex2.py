import librosa
import matplotlib.pyplot as plt


def get_axis(arr):
    return arr[:-1], arr[1:]


def main():

    # load signal
    classical = "data/classical.mp3"
    rock = "data/rock.mp3"

    classical_sig, sr_c = librosa.load(classical, sr=None, duration=20)
    rock_sig, sr_r = librosa.load(rock, sr=None, duration=20)

    # plot signal

    classical_x, classical_y = get_axis(classical_sig)
    rock_x, rock_y = get_axis(rock_sig)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.scatter(classical_x, classical_y, color="blue")
    ax1.set_title("classical plot")
    #    ax1.grid(True)

    ax2.scatter(rock_x, rock_y, color="red")
    ax2.set_title("rock plot")
    #   ax2.grid(True)

    plt.show()


if __name__ == "__main__":
    main()
