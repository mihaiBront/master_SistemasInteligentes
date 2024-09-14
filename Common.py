# -*- coding: utf-8 -*-

import json
import logging as log
import os.path
import types
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, List, Optional

import coloredlogs
import matplotlib.pyplot as plt
from matplotlib import colormaps
import numpy as np
import pandas as pd
import xlwings as xl
from colorama import Fore, Style
import sqlite3 as sql

# region MACROS
# region BCOLORS
BCOLORS = types.SimpleNamespace()
"""
Colors for output printing:

`BCOLORS.HEADER` = '\033[95m'
`BCOLORS.OKBLUE` = '\033[94m'
`BCOLORS.OKCYAN` = '\033[96m'
`BCOLORS.OKGREEN` = '\033[92m'
`BCOLORS.WARNING` = '\033[93m'
`BCOLORS.FAIL` = '\033[91m'
`BCOLORS.ENDC` = '\033[0m'
`BCOLORS.BOLD` = '\033[1m'
`BCOLORS.UNDERLINE` = '\033[4m'
"""

BCOLORS.HEADER = '\033[95m'
BCOLORS.OKBLUE = '\033[94m'
BCOLORS.OKCYAN = '\033[96m'
BCOLORS.OKGREEN = '\033[92m'
BCOLORS.WARNING = '\033[93m'
BCOLORS.FAIL = '\033[91m'
BCOLORS.ENDC = '\033[0m'
BCOLORS.BOLD = '\033[1m'
BCOLORS.UNDERLINE = '\033[4m'
# endregion

# region FileManagement_Vars
TEMP_SUBDIR_NAME = "temp"
# endregion

# region UNIF_DATA_SOURCE_TYPE
UNIF_DATA_SOURCE_TYPE = types.SimpleNamespace()
"""
Type of source for loading data from UNIFORMITY

- `UNIF_SOURCE_TYPE.FieryClrUniX`: ClrUniX.txt file
- `UNIF_SOURCE_TYPE.EISJson`: Log line from Efi Inspection System, containing serialized json object
- `UNIF_SOURCE_TYPE.AVTJson`: Log line from AVT, containing serialized json object
"""
UNIF_DATA_SOURCE_TYPE.FieryClrUniX = "fiery_clrunix"
UNIF_DATA_SOURCE_TYPE.EISJson = "eis_json"
UNIF_DATA_SOURCE_TYPE.AVTJson = "avt_json"

# endregion

# region AMPLITUDE_MODULATION
AMPLITUDE_MODULATION = types.SimpleNamespace()
"""
Macros for Amplitude Modulation type

Returns:
    `AMPLITUDE_MODULATION.Forced` ("forced"): Modulation from a vector inputted by user
    `AMPLITUDE_MODULATION.Automatic` ("auto"): Modulation obtained from level density
"""
AMPLITUDE_MODULATION.VectorForced = "vect_forced"
AMPLITUDE_MODULATION.VectorAuto = "vect_auto"
AMPLITUDE_MODULATION.FunctionForced = "func_forced"
AMPLITUDE_MODULATION.FunctionAuto = "func_auto"
AMPLITUDE_MODULATION.Keep = "zero"
# endregion

# region CLRNAME
CLRNAME: types.SimpleNamespace = types.SimpleNamespace()
"""
Set of macros for helping with channel naming

**Macros**

| Address | Type | Value |
| --- | --- | --- |
| `CLRNAME.Cyan` | `str` | `'cyan'` |
| `CLRNAME.Magenta` | `str` | `'magenta'` |
| `CLRNAME.Yellow` | `str` | `'yellow'` |
| `CLRNAME.Black` | `str` | `'black'` |
| `CLRNAME.Orange` | `str` | `'orange'` |
| `CLRNAME.Violet` | `str` | `'violet'` |
| `CLRNAME.White` | `str` | `'white'` |
"""
CLRNAME.Cyan = 'cyan'
CLRNAME.Magenta = 'magenta'
CLRNAME.Yellow = 'yellow'
CLRNAME.Black = 'black'
CLRNAME.Orange = 'orange'
CLRNAME.Violet = 'violet'
CLRNAME.White = 'white'

CLRVAL: types.SimpleNamespace = types.SimpleNamespace()
CLRVAL.Cyan_RGB = (0, 255, 255)
CLRVAL.Magenta_RGB = (255, 0, 255)
CLRVAL.Yellow_RGB = (255, 255, 0)
CLRVAL.Black_RGB = (0, 0, 0)
CLRVAL.Orange_RGB = (255, 128, 0)
CLRVAL.Violet_RGB = (128, 0, 255)
CLRVAL.White_RGB = (255, 255, 255)

CLRVAL.Cyan_BGR = (255, 255, 0)
CLRVAL.Magenta_BGR = (255, 0, 255)
CLRVAL.Yellow_BGR = (0, 255, 255)
CLRVAL.Black_BGR = (0, 0, 0)
CLRVAL.Orange_BGR = (0, 128, 255)
CLRVAL.Violet_BGR = (255, 0, 128)
CLRVAL.White_BGR = (255, 255, 255)

DICT_fiery_channel_ident: dict = {
    CLRNAME.Cyan: 0,
    CLRNAME.Magenta: 1,
    CLRNAME.Yellow: 2,
    CLRNAME.Black: 3,
    CLRNAME.Orange: 4,
    CLRNAME.Violet: 5
}
"""
Dictionary that relates a channel name with a channel identifier, same channel-ident relation
that fiery uses for its files.

| Macro | Macro Type | Macro Value | Ident (`int`) |
| --- | --- | --- | --- |
| `CLRNAME.Cyan` | `str` | `'cyan'` | 0 |
| `CLRNAME.Magenta` | `str` | `'magenta'` | 1 |
| `CLRNAME.Yellow` | `str` | `'yellow'` | 2 |
| `CLRNAME.Black` | `str` | `'black'` | 3 |
| `CLRNAME.Orange` | `str` | `'orange'` | 4 |
| `CLRNAME.Violet` | `str` | `'violet'` | 5 |
"""
# endregion

# region PROCESSING_TYPE
PROCESSING_TYPE = types.SimpleNamespace()
"""
Macros for specifying signal processing types:

**Types:**

| Processing Method | Type | Value |
|---|---|---|
| `PROCESSING_TYPE.NoFilter` | `str` | `"nofilter"` |
| `PROCESSING_TYPE.Press` | `str` | `"press"` |
| `PROCESSING_TYPE.Bypass` | `str` | `"bypass"` |
| `PROCESSING_TYPE.Flat` | `str` | `"flat"` |

"""
PROCESSING_TYPE.NoFilter = "nofilter"
PROCESSING_TYPE.Press = "press"
PROCESSING_TYPE.Bypass = "bypass"
PROCESSING_TYPE.Flat = "flat"

DICT_processing_types: dict = {
    PROCESSING_TYPE.NoFilter: 0,
    PROCESSING_TYPE.Press: 1,
    PROCESSING_TYPE.Bypass: 2,
    PROCESSING_TYPE.Flat: 3
}
# endregion

# region SOURCE_TYPE
SOURCE_TYPE = types.SimpleNamespace()
"""
Macros for specifying signal source types

**Sources**

| Source | Type | Value | Status |
|---|---|---|---|
| `SOURCE_TYPE.Avt` | `str` | `"avt"` | <colored style="color:red;font-weight:650">not implemented</colored>
| `SOURCE_TYPE.Eis` | `str` | `"eis"` | <colored style="color:red;font-weight:650">not implemented</colored>
| `SOURCE_TYPE.EfiInspectionSystem` | `str` | `"eis"` | <colored style="color:red;font-weight:650">not implemented</colored>
| `SOURCE_TYPE.Fiery` | `str` | `"fiery"` | <colored style="color:red;font-weight:650">not implemented</colored>
| `SOURCE_TYPE.BuffersCompositeForced` | `str` | `"buff"` | operative
| `SOURCE_TYPE.BuffersCompositeDetect` | `str` | `"buff"` | operative
| `SOURCE_TYPE.BuffersMarti` | `str` | `"buff"` | operative
| `SOURCE_TYPE.CompositeForced` | `str` | `"comp_frc"` | operative 
| `SOURCE_TYPE.CompositeDetect` | `str` | `"comp_det"` | operative
| `SOURCE_TYPE.Marti` | `str` | `"mart"` | operative
"""
SOURCE_TYPE.Avt = "avt"
SOURCE_TYPE.Eis = "eis"
SOURCE_TYPE.EfiInspectionSystem = SOURCE_TYPE.Eis
SOURCE_TYPE.Fiery = "fiery"
SOURCE_TYPE.BuffersCompositeForced = "buff_comp_frc"
SOURCE_TYPE.BuffersCompositeDetect = "buff_comp_det"
SOURCE_TYPE.BuffersMarti = "buff_mart"
SOURCE_TYPE.CompositeForced = "comp_frc"
SOURCE_TYPE.CompositeDetect = "comp_det"
SOURCE_TYPE.Marti = "mart"
# endregion

# region EDGE_DETECTION
EDGE_DETECTION = types.SimpleNamespace()
EDGE_DETECTION.RoiInValley = -1
EDGE_DETECTION.RoiInPeak = 1
EDGE_DETECTION.RoiInAny = 0
# endregion

# region COLOR_SPACES
COLOR_SPACE = types.SimpleNamespace()
"""
Macros for specifying color spaces:

**Spaces:**

| Space | Type | Value |
|---|---|---|
| `COLOR_SPACE.RGB` | `str` | `"RGB"` |
| `COLOR_SPACE.BGR` | `str` | `"BGR"` |
| `COLOR_SPACE.HSV` | `str` | `"HSV"` |
| `COLOR_SPACE.HLS` | `str` | `"HSL"` |
| `COLOR_SPACE.XYZ` | `str` | `"XYZ"` |
| `COLOR_SPACE.LAB` | `str` | `"LAB"` |
| `COLOR_SPACE.LCH` | `str` | `"LCH"` |

### `COLOR_SPACE.CHANNEL`

Macros for specifying spaces from color spaces:

| Channel | Type | Value | Color Space |
|---|---|---|---|
| `COLOR_SPACE.CHANNEL.Red` | `str` | `"R"` | `[RGB, BGR]` | 
| `COLOR_SPACE.CHANNEL.Green` | `str` | `"G"` | `[RGB, BGR]` |
| `COLOR_SPACE.CHANNEL.Blue` | `str` | `"B"` | `[RGB, BGR]` | 
| `COLOR_SPACE.CHANNEL.Hue` | `str` | `"H"` | `[HSV, HLS]` | 
| `COLOR_SPACE.CHANNEL.Saturation` | `str` | `"S"` | `[HSV, HLS]` | 
| `COLOR_SPACE.CHANNEL.Value` | `str` | `"V"` | `[HSV]` | 
| `COLOR_SPACE.CHANNEL.Lightness` | `str` | `"L"` | `[HLS]` | 
| `COLOR_SPACE.CHANNEL.X` | `str` | `"X"` | `[XYZ]` | 
| `COLOR_SPACE.CHANNEL.Y` | `str` | `"Y"` | `[XYZ]` | 
| `COLOR_SPACE.CHANNEL.Z` | `str` | `"Z"` | `[XYZ]` | 
| `COLOR_SPACE.CHANNEL.L` | `str` | `"L*"` | `[LAB, LCH]` | 
| `COLOR_SPACE.CHANNEL.nL` | `str` | `"nL*"` | `[LAB, LCH]` |
| `COLOR_SPACE.CHANNEL.A` | `str` | `"A*"` | `[LAB]` |
| `COLOR_SPACE.CHANNEL.B` | `str` | `"B*"` | `[LAB]` |
| `COLOR_SPACE.CHANNEL.C` | `str` | `"C*"` | `[LCH]` |
| `COLOR_SPACE.CHANNEL.H` | `str` | `"H*"` | `[LCH]` |
 
"""
COLOR_SPACE.RGB = "RGB"
COLOR_SPACE.BGR = "BGR"
COLOR_SPACE.HSV = "HSV"
COLOR_SPACE.HLS = "HSL"
COLOR_SPACE.XYZ = "XYZ"
COLOR_SPACE.LAB = "LAB"
COLOR_SPACE.LCH = "LCH"

COLOR_SPACE.CHANNEL = types.SimpleNamespace()
COLOR_SPACE.CHANNEL.Red = "R"
COLOR_SPACE.CHANNEL.Green = "G"
COLOR_SPACE.CHANNEL.Blue = "B"

COLOR_SPACE.CHANNEL.Hue = "H"
COLOR_SPACE.CHANNEL.Saturation = "S"
COLOR_SPACE.CHANNEL.Value = "V"
COLOR_SPACE.CHANNEL.Lightness = "L"

COLOR_SPACE.CHANNEL.X = "X"
COLOR_SPACE.CHANNEL.Y = "Y"
COLOR_SPACE.CHANNEL.Z = "Z"

COLOR_SPACE.CHANNEL.L = "L*"
COLOR_SPACE.CHANNEL.NL = "nL*"
COLOR_SPACE.CHANNEL.A = "A*"
COLOR_SPACE.CHANNEL.B = "B*"

COLOR_SPACE.CHANNEL.C = "C*"
COLOR_SPACE.CHANNEL.H = "H*"

DICT_default_target_channel: dict = {
    COLOR_SPACE.RGB: COLOR_SPACE.CHANNEL.Green,
    COLOR_SPACE.BGR: COLOR_SPACE.CHANNEL.Green,
    COLOR_SPACE.HSV: COLOR_SPACE.CHANNEL.Saturation,
    COLOR_SPACE.HLS: COLOR_SPACE.CHANNEL.Saturation,
    COLOR_SPACE.LAB: COLOR_SPACE.CHANNEL.L,
    COLOR_SPACE.LCH: COLOR_SPACE.CHANNEL.C,
    COLOR_SPACE.XYZ: COLOR_SPACE.CHANNEL.Y
}

DICT_peak_types_for_channel: dict = {
    COLOR_SPACE.CHANNEL.Red: -1,
    COLOR_SPACE.CHANNEL.Green: -1,
    COLOR_SPACE.CHANNEL.Blue: -1,
    COLOR_SPACE.CHANNEL.Hue: -1,
    COLOR_SPACE.CHANNEL.Saturation: -1,
    COLOR_SPACE.CHANNEL.Value: -1,
    COLOR_SPACE.CHANNEL.Lightness: -1,
    COLOR_SPACE.CHANNEL.X: -1,
    COLOR_SPACE.CHANNEL.Y: -1,
    COLOR_SPACE.CHANNEL.Z: -1,
    COLOR_SPACE.CHANNEL.L: 1,
    COLOR_SPACE.CHANNEL.A: -1,
    COLOR_SPACE.CHANNEL.B: -1,
    COLOR_SPACE.CHANNEL.C: -1,
    COLOR_SPACE.CHANNEL.H: -1
}

PIXEL_DEPTH = types.SimpleNamespace()
PIXEL_DEPTH.BIT8 = np.uint8
PIXEL_DEPTH.BIT16 = np.uint16
PIXEL_DEPTH.BIT32 = np.uint32
PIXEL_DEPTH.BIT64 = np.uint64
# endregion

# region INK
INK = types.SimpleNamespace()
"""
Macro namespace structure to hold values for inks, relating ink names with channels

**Macros**

| Channel | Type | Ident |
| --- | --- | --- |
| `INK.Cyan` | `int` | 0 |
| `INK.Magenta` | `int` | 1 |
| `INK.Yellow` | `int` | 2 |
| `INK.Black` | `int` | 3 |
| `INK.Orange` | `int` | 4 |
| `INK.Violet` | `int` | 5 |
| `INK.Unknown` | `int` | -1 |

>`libraries.Uniformity.FieryUniformityMaker.INK.NameToIdent`
>
> Dictionary that relates Channel Names (`str`) with Idents (`int`)

<div/>

>`libraries.Uniformity.FieryUniformityMaker.INK.IdentToName`
>
> Dictionary that relates Channel Idents (`int`) with Names (`str`)
"""

INK.Cyan = 0
INK.Magenta = 1
INK.Yellow = 2
INK.Black = 3
INK.Orange = 4
INK.Violet = 5
INK.Unknown = -1

INK.NameToIdent = {
    "cyan": INK.Cyan,
    "Cyan": INK.Cyan,
    "C": INK.Cyan,
    "c": INK.Cyan,
    "0": INK.Cyan,
    "magenta": INK.Magenta,
    "Magenta": INK.Magenta,
    "M": INK.Magenta,
    "m": INK.Magenta,
    "1": INK.Magenta,
    "yellow": INK.Yellow,
    "Yellow": INK.Yellow,
    "Y": INK.Yellow,
    "y": INK.Yellow,
    "2": INK.Yellow,
    "black": INK.Black,
    "Black": INK.Black,
    "B": INK.Black,
    "b": INK.Black,
    "3": INK.Black,
    "orange": INK.Orange,
    "Orange": INK.Orange,
    "O": INK.Orange,
    "o": INK.Orange,
    "4": INK.Orange,
    "violet": INK.Violet,
    "Violet": INK.Violet,
    "V": INK.Violet,
    "v": INK.Violet,
    "5": INK.Violet
}

INK.IdentToName = {
    INK.Cyan: "cyan",
    INK.Magenta: "magenta",
    INK.Yellow: "yellow",
    INK.Black: "black",
    INK.Orange: "orange",
    INK.Violet: "violet"
}

def INK_NameToFocusChannelLCH(name: str):
    id = -1
    try:
        id = INK.NameToIdent[name]
    except:
        id = -1
    
    needsCstar = [2]
    
    if id in needsCstar:
        return COLOR_SPACE.CHANNEL.C
    else:
        return COLOR_SPACE.CHANNEL.L

# endregion

# region UNIT_CONVERSIONS:
MM_PER_INCH = 24.5
MARGIN_AVERAGE_MULTIPLIER = 3
# endregion
# endregion

class LoggingHelper(object):
    @staticmethod
    def get_logger(level: str = 'INFO'):
        """
        Returns a coloredlogs type logger with the specified level

        Args:
            level (str, optional): Minimum level to be logged 
                [DEBUG > INFO > WARNING > ERROR > FATAL]. 
                Defaults to 'INFO'.

        Returns:
            log: Created logger
        """
        return coloredlogs.install(level=level,
                                   fmt='[%(asctime)s]\t%(levelname)s\t(%(filename)s/%(funcName)s)\t%(message)s',
                                #    datefmt='%H:%M:%S',
                                   level_styles={
                                       'critical': {'bold': True, 'color': 'red'},
                                       'debug': {'color': 'black'},
                                       'error': {'color': 'red'},
                                       'info': {'color': 'cyan'},
                                       'notice': {'color': 'magenta'},
                                       'spam': {'color': 'green', 'faint': True},
                                       'success': {'bold': True, 'color': 'green'},
                                       'verbose': {'color': 'blue'},
                                       'warning': {'color': 'yellow'}
                                       },
                                   field_styles={
                                       'asctime': {'bold': True, 'color': 'black'},
                                       'hostname': {'color': 'magenta'},
                                       'levelname': {'bold': True, 'color': 'black'},
                                       'name': {'bold': True, 'color': 'black'},
                                       'programname': {'bold': True, 'color': 'black'},
                                       'username': {'color': 'yellow'},
                                       'funcName': {'bold': True, 'color': 'black'}
                                       },
                                   isatty=True
                                   )        


class FileManagement(object):
    _workingDir: str
    
    def set_working_dir(self, working_dir: str):
        """
        Sets working directory for an instanciated object for the class

        Args:
            working_dir (str): Directory in which the whole class will work
        """        
        self._workingDir = working_dir
        return
    
    @staticmethod
    def get_dir_from_filepath(path: str) -> str:
        """
        Given any path (either to a file or a directory), returns the parent 
        directory if it is a file, or itself if it is a directory.

        Args:
            path (str): Path

        Returns:
            str: Path to directory
        """
        _path = path[:]
        if "." in path[path.rfind("/"):]:
            _path = path[:path.rfind('/')]
        return _path

    @classmethod
    def create_dir_if_not_exists(cls, dir_path: str) -> str:
        """
        Given a path, creates a directory if it doesn't exists. 
        If the path provided is to a file and not a directory, 
        it creates what would be the parent directory to that file
        
        Args:
            dir_path (str): Path to file or directory

        Returns:
            str: Path to generated path, None if it fails
        """        
        _path = cls.get_dir_from_filepath(dir_path)
        if not os.path.exists(_path):
            try:
                os.mkdir(_path)
                log.debug(f"Created '{_path}' directory.")
            except Exception as ex:
                log.error(f"Failed creating '{_path}' ({ex})")
                return None
        log.debug(f"Directory '{_path}' already existed.")
        return _path
    
    @staticmethod
    def path_to_python(path: str):
        """
        Converts a windows-formatted path to a python-compatible path

        Args
            path (str): File/Directory path
        
        Returns:
            (str) Same path with assured compatibility with python
        """
        return path.replace("\\", "/")
    
    @staticmethod
    def create_temp_folder(path: str, custom_subdir_name: Optional[str] = None):
        """
        Creates temp subdir given a path

        Args:
            path (str): Parent path
            custom_subdir_name: Modifies the temp subdirectory (defaults to '/temp')

        Returns:
            Tuple[str, str]: (Full path to dir, timestamp for files)
        """
        temp_dir = f"{path}/{TEMP_SUBDIR_NAME}"
        if custom_subdir_name is not None:
            temp_dir = f"{path}/{custom_subdir_name}"
        try:
            FileManagement.create_dir_if_not_exists(temp_dir)
        except Exception as ex:
            log.error(f"Failed creating temp folder ({ex})")
            
        return temp_dir, TimeStamp.formatted()
    
    @staticmethod
    def delete_temp_files(path:str, 
                          time_stamp: Optional[str] = None, 
                          custom_subdir_name: Optional[str] =None):
        """
        Removes all temporary files. If time_stamp specified, it will only remove the files with
        said time_stamp, else, it will remove all files inside the dir (files only, not subdirs)
        When function ends, checks if temporary dir is empty, and if so, it deletes it as well.
        
        | Exit Code | Meaning |
        |---|---|
        | -1 | Errors, operation not completed |
        | 0 | Finished deleting only files |
        | 1 | Finished but didn't do anythong |
        | 2 | Finished removing the temp path also |

        Args:
            path (str): Parent directory (where temp. dir is located)
            time_stamp (Optional[str], optional): Specified time stamp, if None, the function 
                will remove all files inside the temp folder. Variable defaults to None.
            custom_subdir_name (Optional[str], optional): In case you have defined a custom subdir
                name for the temporary name, operate on that dir. If not specified, will operate
                onto './temp' Variable defaults to None.

        Returns:
            int: Exit code
        """
        
        temp_dir = f"{path}/{TEMP_SUBDIR_NAME}"
        if custom_subdir_name is not None:
            temp_dir = f"{path}/{custom_subdir_name}"
            
        try:
            temp_files_list = os.listdir(temp_dir)
            temp_files_list = list(filter(lambda x: "." in x, temp_files_list))
            
            if len(temp_files_list) == 0:
                log.debug(f"Temp dir ({temp_dir}) is already empty")
                return 1
            
            if time_stamp is not None:
                try:
                    temp_files_list = list(filter(lambda x: time_stamp in x, temp_files_list))
                    if len(temp_files_list) == 0:
                        log.debug(f"There are no files inside the temp dir ({temp_files_list}) "
                                f"with the specified TimeStamp ({time_stamp})")
                        return 1
                except Exception as ex1:
                    log.error("Failed trying to find any file with the specified "
                            f"TimeStamp ({time_stamp}) inside the temp dir ({temp_dir})")
                    return -1
            
            for file in temp_files_list:
                try:
                    os.remove(f"{temp_dir}/{file}")
                    log.debug(f"Successfully deleted '{file}'")
                except Exception as ex1:
                    log.warning(f"Unable to delete '{file}' ({ex1}), moving on...")
        
        except Exception as ex:
            log.error(f"Failed deleting temp files ({ex})")
            return -1
            
        if len(os.listdir(temp_dir)) == 0:
            try:
                os.rmdir(temp_dir)
                log.debug(f"Dir ({temp_dir}) was empty after process, successfully removed it")
                return 2
            
            except Exception as ex:
                log.error(f"Unable to delete temp dir ({temp_dir}) itself ({ex})")
                return -1
        
        return 0

    @staticmethod
    def isFile(path:str) -> tuple[bool, int]:
        if "/" in path:
            _final_dir = path.split("/")[-1]
        elif "\\" in path:
            _final_dir = path.split("\\")[-1]
        else: return(False, -1)
        
        if not os.path.exists(path):
            return (False, -1)
        
        if "." in _final_dir:
            return True, 0
        else: return False, 0
    
    @classmethod
    def isFolder(cls, path:str) -> tuple[bool, int]:
        ret = cls.isFile(path)
        
        if ret[1] >= 0:
            ret = (not ret[0], ret [1])
            
        return ret
   
    @classmethod
    def getFileExtension(cls, path) -> Optional[str]:
        if not cls.isFile(path)[0]:
            log.warning("Passed path is not a file")
            return None
        
        file = ""
        if "/" in path:
            file = path.split("/")[-1]
        elif "\\" in path:
            file = path.split("\\")[-1]
        else: 
            file = path
        
        return file.split(".")[-1] 
    
    @classmethod
    def checkFileIsValid(cls, path, validExtensions):
        if cls.getFileExtension(path) in validExtensions:
            return True
        else:
            return False       
        
    
class MathAndStatistics(object):
    @staticmethod
    def poly_eval(coefs: list[float], x: float) -> float:
        """
        Evaluates polinomic expression described by "coefs", a coefficient list

        Args:
            coefs (list[float]): List of coefficients from higher power to lower 
                (m_n, m_n-1, m_n-2 ... m_1, n)
            x (float): X point where to evaluate the polinomic function

        Returns:
            float: y, function evaluated at x
        """
        y = 0
        
        for a in coefs:
            y = y*x + a 
        
        return y
    
    @staticmethod
    def simple_amplityde_from_signal(signal: list[float | int] | np.ndarray) -> float:
        """
        In a simple manner, calculates the amplitude of a passed signal (vector)
        As:
            amplitude = 1/2 * (max(signal) - min(signal))

        Args:
            signal (list[float | int] | np.array[float | int]): _description_

        Returns:
            Float: Amplitude
        """
        _ampl = np.max(signal) - np.min(signal)
        _ampl /= 2.0
        return _ampl
    
    @staticmethod
    def remove_outliers_from_signal(data: np.ndarray | list[float], max_stdev: float = 3.0, window_size: int = 30):
        """
        Code that removes outliers from a uniformity level density reading array. Takes every
        value that fall outside of the condition `standard_deviation < m`, and sets them to the 
        value of its surroundings accordding to the window size.
        

        Args:
            data (np.ndarray | list): Uniformity measurements
            max_stdev (float, optional): Maximum accepted standard deviation. Defaults to 3.
            window (int, optional): Window size for returning those values to normal. Defaults 
                to 30.

        Returns:
            np.ndarray | list: Passed data set with the outliers corrected
        """

        _d = np.abs(data - np.median(data))
        _mdev = np.median(_d)
        _s = _d/_mdev if _mdev else np.zeros(len(_d))
        
        data_removed = [data[i] if _s[i] < max_stdev 
                        else np.average(np.concatenate(
                            (data[i- window_size//2: i - 1], 
                                data[i + 1: i + window_size//2]))) 
                        for i in range(len(data))]    
            
        return data_removed        


class TimeStamp(object):
    @staticmethod
    def formatted(timestamp_format: str = "%Y%m%d_%H%M%S") -> str:
        """
        Generates a timestamp in a certain format (defaulting to 'YYYYmmdd_HHMMSS') 
        for the time when it is called

        Args:
            timestamp_format (str, optional): Format for the timestamp. Defaults to "%Y%m%d_%H%M%S".

        Returns:
            str: Time stamp in text form
        """
        return datetime.fromtimestamp(datetime.now().timestamp()).strftime(timestamp_format)


class Serializable(FileManagement):
    """
    Abstract class for classes that have to be serializable. Includes methods for working with
    text JSONs, as well as some extra comodity methods for excluding private elements from 
    those JSON strings, passing a reference to the possible outer class of an inner one, and a
    config dialog (most of the abstract methods comming empty)
    """
    _outer: Any = field(default=None)

    def exclude_private(self) -> dict:
        """
        Excludes private properties from dictionary for JSON serialization

        :return: (dict) Filtered dictionary
        """
        no_private: dict = self.__dict__.copy()
        keys_to_pop = list([key for key, val in self.__dict__.items() if key[0] == "_"])
        for key in keys_to_pop:
            no_private.pop(key)
        return no_private

    @classmethod    # FIXME: should be private but have to fix class parity in InspectionLibEfi first
    def from_dict(cls, self: Any) -> Optional[object]:
        """
        Helper class for deserializing JSONs

        Args:
            self (Any): Any type object, used to help deserialization
        
        Returns:
            object: Object of current class with info from json string
        """
        log.warning("This class does not implement this method")
        return None

    @classmethod
    def deserialize(cls, json_string: str) -> object:
        """
        Deserializes JSON string to object according to the cls.from_dict method

        Args:
            json_string (str): Serialized object
        
        Returns:
            object: Object from json
        """

        _obj: type(cls) = cls.from_dict(json.loads(json_string)) # type: ignore
        return _obj

    def serialize(self) -> str:
        """
        Serializes object in a JSON format (excluding private parameters)

        Returns:
            str: Serialized object
        """
        return json.dumps(self, default=lambda o: o.exclude_private(), sort_keys=False, indent=4)

    @classmethod
    def from_file(cls, json_file_path: str):
        """
        Gets JSON from file, and deserializes it to current object class
        
        Args:
            json_file_path (str): Res to JSON file
        
        Returns:
            (object): Deserialized from JSON
        """
        try:
            with open(cls.path_to_python(json_file_path)) as file:
                json_string = file.read()
        except Exception as ex:
            log.error(f"Couldn't open or read '{json_file_path}' ({ex}). Aborted")
            return None

        if json_string is None:
            log.error("Text from file is None. Aborted")
            return None

        json_obj = None

        try:
            json_obj = cls.deserialize(json_string)
        except Exception as ex:
            log.warning(f"Failed getting object from '{json_file_path}' ({ex})")

        if json_obj is None:
            log.error("Unable to deserialize json (is none)")
            return None

        log.info("Deserialized object correctly")
        return json_obj

    def to_file(self, file_path: str):
        """
        Saves an object onto a specified file

        :param file_path: (str) Res to file where to save the object, serialized as json
        :return: (str) Returns file_path back
        """

        file_path = self.path_to_python(file_path)

        # check if a file extension was specified
        if "." not in file_path:
            log.warning("The path specified has no file extension. File not saved")
            return None

        # check if path to dir existed
        dir_path = file_path[:file_path.rfind("/")]

        if not os.path.exists(dir_path):
            log.info(f"Dir didn't exist. Created '{dir_path}'")
            os.mkdir(dir_path)

        with open(file_path, "w") as file:
            file.write(self.serialize())
            log.info("Object successfully saved on file")

        return file_path

    @classmethod
    def config_dialog(cls):
        """
        Launches a configuration dialog that asks for user input for each parameter from the class. Returns an object
        """

        log.error("This class does not implement this method")
        pass

    def pass_outer(self, outer):
        """
        Passes outer object to inner, and stores it inside the private property 'cls._outer'

        Args:
            outer (object): Outer object
        """

        self._outer = outer


class Plotting(object):
    @staticmethod
    def plotSetOfSignals(signal_set: list[np.ndarray], signal_colors: list[str], x_signal_set: Optional[list[np.ndarray]] = None, signal_names: Optional[List[str]] = None,
                         plot_title: Optional[str] = None, x_axis_title: Optional[str] = None, y_axis_title: Optional[str] = None, figsize: Optional[tuple[int, int]] = None,
                         alphas = None, dump_plot_path: Optional[str] = None, show_plot = True):
                        
        if figsize is not None:
            plt.figure(figsize=figsize)
            
        if x_signal_set is None:
            log.warning("x set validations failed, defaulting to linspace...")
            x_signal_set = [range(len(signal_set[0])) for signal in signal_set]                
        
        if not isinstance(alphas, list) or alphas is None:
            if isinstance(alphas, int) or isinstance(alphas, float):
                alphas = np.ones(len(signal_set)) * alphas
            else:
                alphas = np.ones(len(signal_set))
        elif len(alphas) != len(signal_set):
                alphas = np.ones(len(signal_set)) * alphas[0]
        
        if plot_title is None:
            plot_title = "Plot"
        
        if x_axis_title is None:
            x_axis_title = "X axis"
            
        if y_axis_title is None:
            y_axis_title = "X axis"
        
        for signal in range(len(signal_set)):
            plt.plot(x_signal_set[signal], signal_set[signal], label=signal_names[signal], color=signal_colors[signal], alpha=alphas[signal])
        
        plt.legend()
        plt.title(plot_title)
        plt.xlabel(x_axis_title)
        plt.ylabel(y_axis_title)
        
        if dump_plot_path is not None:
            plt.savefig(dump_plot_path)
        
        if show_plot:
            plt.show()
        
        return


class DataDumping():
    @staticmethod
    def dump_matrix_to_file(matrix: list[list], output_path: str, index = False):
         df = pd.DataFrame(np.transpose(matrix), columns=[i for i in range(len(matrix))])
         df.to_excel(output_path, index=index)


class DescriptiveStrPrint(object):
    pass


class SqlMethods(object):
    cursor: sql.Cursor
    
    def __init__(path):
        #create connection and cursor
        pass
    
    def getColumnsFromTable(self, columns:list[str]):
        pass
    
    def getAllFromTable(self):
        pass


def betterPrint(msg:str, color: str):
    """_summary_

    Args:
        msg (str): Message to print
        color (str): Color information
    """
    print(f"{color}{msg}{BCOLORS.ENDC}")
    return