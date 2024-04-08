# EDMD-DL using NODEs

An implementation of [Extended dynamic mode decomposition with dictionary learning using neural ordinary differential equations](https://www.jstage.jst.go.jp/article/nolta/12/4/12_626/_article) proposed by Hiroaki Terao, Sho Shirasaka and Hideyuki Suzuki.

## Usage
- Please prepare time series data of your concerning dynamical system as CSV files. The script used to output the data for the system discussed in our paper is located in the data directory.
- `NODE-EDMD-DL.py` implements our proposed method. For the first round of training, you need to comment out the lines 74-79 in `NODE-EDMD-DL.py`. These lines are responsible for loading `.pkl` files, which contain information about the input layer, hidden layers, and output layer when the loss is minimized. Since these files are generated during the training, they will not be available at the beginning of your first training session. It is easy to automate the process of checking for the existence of these `.pkl` files but we haven't. I apologize for any inconvenience our laziness may cause.


## Notes

No revisions or refinements have been applied to the code since its creation up to 2021.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

This project includes code that is licensed under the MIT License from the work of [Jeff Whitaker](https://github.com/jswhit/pyks/). For more details, see the license information in the headers of the corresponding codes ([data/KS.py](data/KS.py),[data/KSanimate.py](data/KSanimate.py)).
