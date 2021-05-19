from gym_combat.envs.Common.constants import *
import os

class fixed_state_berlin():
    def __init__(self):
        self.qs_0 = []
        self.qs_1 = []
        self.qs_2 = []
        self.qs_3 = []
        self.qs_4 = []
        self.qs_5 = []
        self.qs_6 = []
        self.qs_7 = []
        self.qs_8 = []
        self.fixed_state = self.set_fixed_state()



    def set_fixed_state(self):
        if not DSM_name=="100X100_Berlin":
            return
        a0 = [[0.], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.], [0.],
              [0.05882353], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.39215687], [0.39215687],
              [0.39215687], [0.39215687], [0.39215687]]
        a1 = [[0.], [0.], [0.], [0.], [0.], [0.39215687], [0.], [0.], [0.], [0.], [0.], [0.], [0.05882353], [0.],
              [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.], [0.39215687],
              [0.39215687], [0.39215687], [0.39215687], [0.39215687]]
        a2 = [[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.], [0.05882353],
              [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.],
              [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.]]
        a3 = [[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.39215687],
              [0.05882353], [0.05882353], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.39215687],
              [0.39215687], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.]]
        a4 = [[0.], [0.], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687],
              [0.], [0.05882353], [0.05882353], [0.05882353], [0.05882353], [0.39215687], [0.39215687], [0.39215687],
              [0.39215687], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.]]
        a5 = [[0.], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.39215687], [0.39215687],
              [0.39215687], [0.], [0.], [0.05882353], [0.05882353], [0.05882353], [0.05882353], [0.39215687],
              [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687],
              [0.39215687]]
        a6 = [[0.], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.39215687], [0.39215687],
              [0.39215687], [0.], [0.], [0.05882353], [0.05882353], [0.05882353], [0.05882353], [0.39215687],
              [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687],
              [0.39215687]]
        a7 = [[0.], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.39215687], [0.39215687],
              [0.39215687], [0.39215687], [0.], [0.05882353], [0.05882353], [0.05882353], [0.05882353], [0.39215687],
              [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687],
              [0.39215687]]
        a8 = [[0.], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.39215687],
              [0.39215687], [0.39215687], [0.39215687], [0.], [0.05882353], [0.05882353], [0.05882353], [0.05882353],
              [0.05882353], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.39215687],
              [0.39215687], [0.39215687]]
        a9 = [[0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.39215687], [0.39215687],
              [0.39215687], [0.39215687], [0.], [0.05882353], [0.05882353], [0.05882353], [0.05882353], [0.05882353],
              [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.39215687], [0.39215687],
              [0.39215687]]
        a10 = [[0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.39215687], [0.39215687],
               [0.39215687], [0.39215687], [0.], [0.], [0.05882353], [0.05882353], [0.05882353], [0.05882353],
               [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.39215687], [0.39215687],
               [0.39215687]]
        a11 = [[0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.39215687],
               [0.39215687], [0.39215687], [0.], [0.], [0.05882353], [0.05882353], [0.05882353], [0.05882353],
               [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.39215687], [0.39215687],
               [0.39215687]]
        a12 = [[0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.39215687],
               [0.39215687], [0.39215687], [0.39215687], [0.], [0.05882353], [0.05882353], [0.05882353], [0.05882353],
               [0.05882353], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.], [0.39215687],
               [0.39215687]]
        a13 = [[0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.39215687], [0.39215687],
               [0.39215687], [0.39215687], [0.], [0.11372549], [0.05882353], [0.05882353], [0.05882353], [0.05882353],
               [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.], [0.], [0.]]
        a14 = [[0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.39215687],
               [0.39215687], [0.39215687], [0.39215687], [0.], [0.05882353], [0.20392157], [0.05882353], [0.05882353],
               [0.05882353], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.], [0.]]
        a15 = [[0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.39215687],
               [0.39215687], [0.39215687], [0.39215687], [0.], [0.20392157], [0.20392157], [0.20392157], [0.20392157],
               [0.20392157], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.], [0.]]
        a16 = [[0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.39215687],
               [0.39215687], [0.39215687], [0.], [0.20392157], [0.20392157], [0.20392157], [0.20392157], [0.20392157],
               [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.], [0.39215687]]
        a17 = [[0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.39215687],
               [0.39215687], [0.39215687], [0.39215687], [0.], [0.20392157], [0.20392157], [0.20392157], [0.20392157],
               [0.20392157], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.39215687], [0.39215687]]
        a18 = [[0.], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.39215687], [0.39215687],
               [0.39215687], [0.39215687], [0.], [0.20392157], [0.20392157], [0.20392157], [0.20392157], [0.20392157],
               [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.39215687], [0.39215687]]
        a19 = [[0.], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.39215687],
               [0.39215687], [0.39215687], [0.39215687], [0.], [0.20392157], [0.20392157], [0.20392157], [0.20392157],
               [0.20392157], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.39215687],
               [0.39215687]]
        a20 = [[0.], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.39215687],
               [0.39215687], [0.39215687], [0.39215687], [0.], [0.20392157], [0.20392157], [0.20392157], [0.20392157],
               [0.20392157], [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.39215687]]
        a21 = [[0.], [0.], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.39215687], [0.39215687],
               [0.39215687], [0.39215687], [0.20392157], [0.20392157], [0.20392157], [0.20392157], [0.20392157],
               [0.20392157], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.39215687]]
        a22 = [[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687],
               [0.39215687], [0.20392157], [0.20392157], [0.20392157], [0.20392157], [0.20392157], [0.20392157],
               [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.39215687]]
        a23 = [[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687],
               [0.39215687], [0.20392157], [0.20392157], [0.20392157], [0.20392157], [0.20392157], [0.20392157],
               [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.], [0.39215687]]
        a24 = [[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687],
               [0.39215687], [0.29803923], [0.20392157], [0.20392157], [0.20392157], [0.20392157], [0.20392157],
               [0.39215687], [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.]]
        a25 = [[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.39215687], [0.39215687], [0.39215687],
               [0.39215687], [0.39215687], [0.], [0.20392157], [0.20392157], [0.20392157], [0.20392157], [0.39215687],
               [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.]]
        a26 = [[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.39215687], [0.39215687],
               [0.39215687], [0.39215687], [0.], [0.], [0.20392157], [0.20392157], [0.20392157], [0.39215687],
               [0.39215687], [0.39215687], [0.39215687], [0.], [0.], [0.]]
        s_a = np.array(
            [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22,
             a23, a24, a25, a26])

        return s_a


    def fllow_states(self, qss, SAVE=False, save_folder_path=None):
        if not DSM_name=="100X100_Berlin":
            return
        # plt.matshow(s_a)

        qs = qss[0]
        self.qs_0.append(qs[0])
        self.qs_1.append(qs[1])
        self.qs_2.append(qs[2])
        self.qs_3.append(qs[3])
        self.qs_4.append(qs[4])
        self.qs_5.append(qs[5])
        self.qs_6.append(qs[6])
        self.qs_7.append(qs[7])
        self.qs_8.append(qs[8])

        if SAVE:
            self.save_figure(save_folder_path)

    def save_figure(self, save_folder_path):

        fig, ax = plt.subplots(3, 4)
        plt.tight_layout()

        ax[0, 0].plot(self.qs_0)
        ax[0, 0].set_title("Top Left")
        ax[0, 0].axis([0, len(self.qs_0), -2, 2])
        ax[1, 0].plot(self.qs_1)
        ax[1, 0].set_title("Top Right")
        ax[1, 0].axis([0, len(self.qs_0), -2, 2])
        ax[2, 0].plot(self.qs_2)
        ax[2, 0].set_title("Right")
        ax[2, 0].axis([0, len(self.qs_0), -2, 2])

        ax[0, 1].plot(self.qs_3)
        ax[0, 1].set_title("Bottom Right")
        ax[0, 1].axis([0, len(self.qs_0), -2, 2])
        ax[1, 1].plot(self.qs_4)
        ax[1, 1].set_title("Bottom")
        ax[1, 1].axis([0, len(self.qs_0), -2, 2])
        ax[2, 1].plot(self.qs_5)
        ax[2, 1].set_title("Stay")
        ax[2, 1].axis([0, len(self.qs_0), -2, 2])

        ax[0, 2].plot(self.qs_6)
        ax[0, 2].set_title("Top")
        ax[0, 2].axis([0, len(self.qs_0), -2, 2])
        ax[1, 2].plot(self.qs_7)
        ax[1, 2].set_title("Bottom Left")
        ax[1, 2].axis([0, len(self.qs_0), -2, 2])
        ax[2, 2].plot(self.qs_8)
        ax[2, 2].set_title("Left")
        ax[2, 2].axis([0, len(self.qs_0), -2, 2])

        ax9 = plt.subplot(133)
        ax9.matshow(self.fixed_state)

        #plt.show()
        plt.savefig(save_folder_path + os.path.sep + 'q_values')
        plt.close()