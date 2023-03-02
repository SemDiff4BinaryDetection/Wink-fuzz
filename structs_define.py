from ctypes import * 
import ctypes 
from sys import getsizeof 
from pdb import set_trace as bp 
from ctypes.wintypes import * 
#from _multiprocessing import win32 
import argparse


class NtRemoveIoCompletionEx_arg2_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtRemoveIoCompletionEx_arg2_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtRemoveIoCompletionEx_arg2_struct2),
                 ("reserve3", ULONG)
                )

class NtRemoveIoCompletionEx_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", POINTER(NtRemoveIoCompletionEx_arg2_struct1)),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                )
class NtRemoveIoCompletionEx_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtUserEnumDisplaySettings_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT)
                ]
class NtFlushBuffersFileEx_arg5_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtGdiStartDoc_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", c_char_p),
                 ("reserve2", c_char_p),
                 ("reserve3", c_char_p),
                 ("reserve4", ULONG)
                ]
class NtUserGetCursorInfo_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserGetCursorInfo_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtUserGetCursorInfo_arg1_struct1)
                )
class NtUserPeekMessage_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserPeekMessage_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", POINTER(ULONG)),
                 ("reserve4", ULONG),
                 ("reserve5", NtUserPeekMessage_arg1_struct1),
                 ("reserve6", ULONG)
                )
class NtUserGetRegisteredRawInputDevices_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtSetQuotaInformationFile_arg2_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtGdiBRUSHOBJ_DeleteRbrush_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtGdiBRUSHOBJ_DeleteRbrush_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtGdiDdDDISetMonitorColorSpaceTransform_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDISetMonitorColorSpaceTransform_arg1_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]

class NtGdiDdDDISetMonitorColorSpaceTransform_arg1_struct2(ctypes.Structure):
     _fields_ = (("reserve0", ULONG*12),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiDdDDISetMonitorColorSpaceTransform_arg1_struct3*4096)
                )

class NtGdiDdDDISetMonitorColorSpaceTransform_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiDdDDISetMonitorColorSpaceTransform_arg1_struct1),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(NtGdiDdDDISetMonitorColorSpaceTransform_arg1_struct2))
                )
class NtGdiGetTextExtentExW_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtRIMGetDeviceProperties_arg3_struct4(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT)
                ]

class NtRIMGetDeviceProperties_arg3_struct3(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT)
                ]

class NtRIMGetDeviceProperties_arg3_struct2(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE)
                ]

class NtRIMGetDeviceProperties_arg3_struct1(ctypes.Structure):
     _fields_ = (("reserve0", NtRIMGetDeviceProperties_arg3_struct2),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", ULONG),
                 ("reserve6", NtRIMGetDeviceProperties_arg3_struct3),
                 ("reserve7", NtRIMGetDeviceProperties_arg3_struct4)
                )

class NtRIMGetDeviceProperties_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtRIMGetDeviceProperties_arg3_struct1)
                )
class NtGdiEngCheckAbort_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngCheckAbort_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngCheckAbort_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtWaitForDebugEvent_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtWaitForDebugEvent_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetRawInputDeviceList_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserInjectMouseInput_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]
class NtGdiDdDDIDestroyDevice_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIWaitForVerticalBlankEvent2_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG*8)
                ]
class NtDuplicateToken_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtDuplicateToken_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtDuplicateToken_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiFONTOBJ_pvTrueTypeFontFile_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiFONTOBJ_pvTrueTypeFontFile_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", NtGdiFONTOBJ_pvTrueTypeFontFile_arg1_struct1),
                 ("reserve7", ULONG),
                 ("reserve8", POINTER(ULONG)),
                 ("reserve9", POINTER(ULONG))
                ]
class NtGdiDdDDISetFSEBlock_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDISetFSEBlock_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiDdDDISetFSEBlock_arg1_struct1),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                )
class NtUserSetFeatureReportResponse_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", ULONG),
                 ("reserve3", USHORT)
                ]
class NtGdiEngLineTo_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngLineTo_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngLineTo_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngLineTo_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngLineTo_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiEngLineTo_arg2_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtGdiEngLineTo_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtGdiEngLineTo_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUserInjectTouchInput_arg2_struct7(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtUserInjectTouchInput_arg2_struct6(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtUserInjectTouchInput_arg2_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserInjectTouchInput_arg2_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserInjectTouchInput_arg2_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserInjectTouchInput_arg2_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserInjectTouchInput_arg2_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", NtUserInjectTouchInput_arg2_struct2),
                 ("reserve7", NtUserInjectTouchInput_arg2_struct3),
                 ("reserve8", NtUserInjectTouchInput_arg2_struct4),
                 ("reserve9", NtUserInjectTouchInput_arg2_struct5),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG)
                )

class NtUserInjectTouchInput_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtUserInjectTouchInput_arg2_struct1),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtUserInjectTouchInput_arg2_struct6),
                 ("reserve4", NtUserInjectTouchInput_arg2_struct7),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                )
class NtCreateMutant_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateMutant_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtCreateMutant_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateMutant_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", USHORT),
                 ("reserve7", USHORT),
                 ("reserve8", c_char_p)
                ]
class NtLockVirtualMemory_arg2_struct0(Structure):
     _fields_ = [("reserve0", LPVOID)
                ]
class NtLockVirtualMemory_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetComboBoxInfo_arg2_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtUserGetComboBoxInfo_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtUserGetComboBoxInfo_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtUserGetComboBoxInfo_arg2_struct1),
                 ("reserve2", NtUserGetComboBoxInfo_arg2_struct2),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                )
class NtGdiDdDDIOutputDuplGetFrameInfo_arg1_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDIOutputDuplGetFrameInfo_arg1_struct2(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiDdDDIOutputDuplGetFrameInfo_arg1_struct3),
                 ("reserve1", ULONG)
                )

class NtGdiDdDDIOutputDuplGetFrameInfo_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", NtGdiDdDDIOutputDuplGetFrameInfo_arg1_struct2),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG)
                )

class NtGdiDdDDIOutputDuplGetFrameInfo_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiDdDDIOutputDuplGetFrameInfo_arg1_struct1)
                )
class NtUserGetPointerDeviceCursors_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserSetWinEventHook_arg4_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtUserSetWinEventHook_arg4_struct0(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtUserSetWinEventHook_arg4_struct1))
                )
class NtGdiDdDDISetSyncRefreshCountWaitTarget_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiGetTransform_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]
class NtUserTransformRect_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIDestroyKeyedMutex_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIPresentMultiPlaneOverlay_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIPresentMultiPlaneOverlay_arg1_struct6(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIPresentMultiPlaneOverlay_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIPresentMultiPlaneOverlay_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIPresentMultiPlaneOverlay_arg1_struct7(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIPresentMultiPlaneOverlay_arg1_struct3(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDIPresentMultiPlaneOverlay_arg1_struct4),
                 ("reserve2", NtGdiDdDDIPresentMultiPlaneOverlay_arg1_struct5),
                 ("reserve3", NtGdiDdDDIPresentMultiPlaneOverlay_arg1_struct6),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", POINTER(NtGdiDdDDIPresentMultiPlaneOverlay_arg1_struct7)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG)
                )

class NtGdiDdDDIPresentMultiPlaneOverlay_arg1_struct2(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiDdDDIPresentMultiPlaneOverlay_arg1_struct3)
                )

class NtGdiDdDDIPresentMultiPlaneOverlay_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG*64),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", NtGdiDdDDIPresentMultiPlaneOverlay_arg1_struct1),
                 ("reserve7", ULONG),
                 ("reserve8", POINTER(NtGdiDdDDIPresentMultiPlaneOverlay_arg1_struct2)),
                 ("reserve9", ULONG)
                )
class NtQueryQuotaInformationFile_arg2_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtQueryQuotaInformationFile_arg8_struct1(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtQueryQuotaInformationFile_arg8_struct0(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtQueryQuotaInformationFile_arg8_struct1),
                 ("reserve3", ULONG*1024)
                ]
class NtGdiDdDDIOpenSyncObjectFromNtHandle_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserUnregisterClass_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserUnregisterClass_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtApphelpCacheControl_arg2_struct1(Structure):
     _fields_ = [("reserve0", c_char*2048)
                ]

class NtApphelpCacheControl_arg2_struct2(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtApphelpCacheControl_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG),
                 ("reserve23", ULONG),
                 ("reserve24", ULONG),
                 ("reserve25", ULONG),
                 ("reserve26", ULONG),
                 ("reserve27", ULONG),
                 ("reserve28", ULONG),
                 ("reserve29", ULONG),
                 ("reserve30", ULONG),
                 ("reserve31", USHORT),
                 ("reserve32", USHORT),
                 ("reserve33", POINTER(NtApphelpCacheControl_arg2_struct1)),
                 ("reserve34", ULONG),
                 ("reserve35", ULONG),
                 ("reserve36", ULONG),
                 ("reserve37", ULONG),
                 ("reserve38", ULONG),
                 ("reserve39", ULONG),
                 ("reserve40", ULONG),
                 ("reserve41", ULONG),
                 ("reserve42", ULONG),
                 ("reserve43", ULONG),
                 ("reserve44", ULONG),
                 ("reserve45", ULONG),
                 ("reserve46", ULONG),
                 ("reserve47", ULONG),
                 ("reserve48", POINTER(NtApphelpCacheControl_arg2_struct2)),
                 ("reserve49", ULONG)
                )
class NtGdiDescribePixelFormat_arg4_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", ULONG),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE),
                 ("reserve6", BYTE),
                 ("reserve7", BYTE),
                 ("reserve8", BYTE),
                 ("reserve9", BYTE),
                 ("reserve10", BYTE),
                 ("reserve11", BYTE),
                 ("reserve12", BYTE),
                 ("reserve13", BYTE),
                 ("reserve14", BYTE),
                 ("reserve15", BYTE),
                 ("reserve16", BYTE),
                 ("reserve17", BYTE),
                 ("reserve18", BYTE),
                 ("reserve19", BYTE),
                 ("reserve20", BYTE),
                 ("reserve21", BYTE),
                 ("reserve22", BYTE),
                 ("reserve23", ULONG),
                 ("reserve24", ULONG),
                 ("reserve25", ULONG)
                ]
class NtGdiFONTOBJ_pQueryGlyphAttrs_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiFONTOBJ_pQueryGlyphAttrs_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", NtGdiFONTOBJ_pQueryGlyphAttrs_arg1_struct1),
                 ("reserve7", ULONG),
                 ("reserve8", POINTER(ULONG)),
                 ("reserve9", POINTER(ULONG))
                ]
class NtGdiConvertMetafileRect_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiDdDDIReleaseKeyedMutex_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtOpenRegistryTransaction_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenRegistryTransaction_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenRegistryTransaction_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiDdDDIUnlock_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG))
                ]
class NtSetTimerResolution_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtSetSystemEnvironmentValueEx_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtSetSystemEnvironmentValueEx_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", BYTE*8)
                ]
class NtGdiDdDDIAcquireKeyedMutex_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(c_longlong)),
                 ("reserve3", ULONG)
                ]
class NtGdiEngTransparentBlt_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngTransparentBlt_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngTransparentBlt_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngTransparentBlt_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngTransparentBlt_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngTransparentBlt_arg2_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngTransparentBlt_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngTransparentBlt_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiEngTransparentBlt_arg3_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtGdiEngTransparentBlt_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiEngTransparentBlt_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiEngTransparentBlt_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiPolyTextOutW_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiPolyTextOutW_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", c_char_p),
                 ("reserve4", ULONG),
                 ("reserve5", NtGdiPolyTextOutW_arg2_struct1),
                 ("reserve6", POINTER(ULONG))
                ]
class NtGdiSTROBJ_dwGetCodePage_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiSTROBJ_dwGetCodePage_arg1_struct6(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiSTROBJ_dwGetCodePage_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiSTROBJ_dwGetCodePage_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiSTROBJ_dwGetCodePage_arg1_struct3(Structure):
     _fields_ = [("reserve0", NtGdiSTROBJ_dwGetCodePage_arg1_struct4),
                 ("reserve1", NtGdiSTROBJ_dwGetCodePage_arg1_struct5),
                 ("reserve2", BYTE*1)
                ]

class NtGdiSTROBJ_dwGetCodePage_arg1_struct2(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", LPVOID),
                 ("reserve2", NtGdiSTROBJ_dwGetCodePage_arg1_struct6)
                )

class NtGdiSTROBJ_dwGetCodePage_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiSTROBJ_dwGetCodePage_arg1_struct1),
                 ("reserve4", POINTER(NtGdiSTROBJ_dwGetCodePage_arg1_struct2)),
                 ("reserve5", c_char_p)
                ]
class NtDeleteValueKey_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserChangeDisplaySettings_arg2_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT)
                ]

class NtUserChangeDisplaySettings_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", c_char*72),
                 ("reserve1", ULONG),
                 ("reserve2", NtUserChangeDisplaySettings_arg2_struct1),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", USHORT),
                 ("reserve6", USHORT),
                 ("reserve7", USHORT),
                 ("reserve8", USHORT),
                 ("reserve9", USHORT),
                 ("reserve10", USHORT),
                 ("reserve11", USHORT),
                 ("reserve12", c_char*66),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG),
                 ("reserve23", ULONG),
                 ("reserve24", ULONG),
                 ("reserve25", ULONG)
                )
class NtGdiGetDIBitsInternal_arg6_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG)
                ]

class NtGdiGetDIBitsInternal_arg6_struct0(Structure):
     _fields_ = [("reserve0", NtGdiGetDIBitsInternal_arg6_struct1),
                 ("reserve1", ULONG*1)
                ]
class NtGdiSTROBJ_bGetAdvanceWidths_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiSTROBJ_bGetAdvanceWidths_arg1_struct6(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiSTROBJ_bGetAdvanceWidths_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiSTROBJ_bGetAdvanceWidths_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiSTROBJ_bGetAdvanceWidths_arg1_struct3(Structure):
     _fields_ = [("reserve0", NtGdiSTROBJ_bGetAdvanceWidths_arg1_struct4),
                 ("reserve1", NtGdiSTROBJ_bGetAdvanceWidths_arg1_struct5),
                 ("reserve2", BYTE*1)
                ]

class NtGdiSTROBJ_bGetAdvanceWidths_arg1_struct2(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", LPVOID),
                 ("reserve2", NtGdiSTROBJ_bGetAdvanceWidths_arg1_struct6)
                )

class NtGdiSTROBJ_bGetAdvanceWidths_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiSTROBJ_bGetAdvanceWidths_arg1_struct1),
                 ("reserve4", POINTER(NtGdiSTROBJ_bGetAdvanceWidths_arg1_struct2)),
                 ("reserve5", c_char_p)
                ]
class NtGdiSTROBJ_bGetAdvanceWidths_arg4_struct0(Structure):
     _fields_ = [("reserve0", c_longlong),
                 ("reserve1", c_longlong)
                ]
class NtGdiDdDDISharedPrimaryUnLockNotification_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDISharedPrimaryUnLockNotification_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiDdDDISharedPrimaryUnLockNotification_arg1_struct1),
                 ("reserve1", ULONG)
                )
class NtQuerySystemInformationEx_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIWaitForSynchronizationObject_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG*32),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG),
                 ("reserve23", ULONG),
                 ("reserve24", ULONG),
                 ("reserve25", ULONG),
                 ("reserve26", ULONG),
                 ("reserve27", ULONG),
                 ("reserve28", ULONG),
                 ("reserve29", ULONG),
                 ("reserve30", ULONG),
                 ("reserve31", ULONG),
                 ("reserve32", ULONG),
                 ("reserve33", ULONG),
                 ("reserve34", c_longlong*8),
                 ("reserve35", ULONG),
                 ("reserve36", ULONG),
                 ("reserve37", ULONG),
                 ("reserve38", ULONG),
                 ("reserve39", ULONG),
                 ("reserve40", ULONG),
                 ("reserve41", ULONG),
                 ("reserve42", ULONG),
                 ("reserve43", ULONG),
                 ("reserve44", ULONG),
                 ("reserve45", ULONG),
                 ("reserve46", ULONG),
                 ("reserve47", ULONG),
                 ("reserve48", ULONG),
                 ("reserve49", ULONG)
                ]
class NtGdiDdDDIGetSharedPrimaryHandle_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtQuerySecurityAttributesToken_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtQuerySecurityAttributesToken_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtQuerySecurityAttributesToken_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIPresentRedirected_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]

class NtGdiDdDDIPresentRedirected_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiDdDDIPresentRedirected_arg1_struct1)
                )
class NtAlpcQueryInformation_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetMouseMovePointsEx_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUserGetMouseMovePointsEx_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiDdDDIOpenKeyedMutex_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiAddRemoteMMInstanceToDC_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG*16)
                ]

class NtGdiAddRemoteMMInstanceToDC_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiAddRemoteMMInstanceToDC_arg2_struct1)
                )
class NtCreateEnlistment_arg5_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtCreateEnlistment_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateEnlistment_arg5_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtUserScrollWindowEx_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUserScrollWindowEx_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUserScrollWindowEx_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUnloadKey_arg1_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtUnloadKey_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtUnloadKey_arg1_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                )
class NtGdiDdDDIOpenSyncObjectFromNtHandle2_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIOpenSyncObjectFromNtHandle2_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiDdDDIOpenSyncObjectFromNtHandle2_arg1_struct1),
                 ("reserve3", ULONG),
                 ("reserve4", c_longlong*8)
                ]
class NtUserGetIconInfo_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG)
                ]
class NtUserGetIconInfo_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserGetIconInfo_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetIconInfo_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserLoadKeyboardLayoutEx_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserLoadKeyboardLayoutEx_arg6_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGetNextThread_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetAtomName_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtUserGetAtomName_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtUserGetAtomName_arg2_struct1))
                )
class NtGdiCreateSessionMappedDIBSection_arg4_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG)
                ]

class NtGdiCreateSessionMappedDIBSection_arg4_struct0(Structure):
     _fields_ = [("reserve0", NtGdiCreateSessionMappedDIBSection_arg4_struct1),
                 ("reserve1", ULONG*1)
                ]
class NtGdiGetEmbUFI_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG*16)
                ]
class NtOpenDirectoryObject_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenDirectoryObject_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenDirectoryObject_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiDdDDISetStablePowerState_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiEngDeleteClip_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngDeleteClip_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiEngDeleteClip_arg1_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtOpenTransaction_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenTransaction_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenTransaction_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtOpenTransaction_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]
class NtGetMUIRegistryInfo_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiBRUSHOBJ_pvAllocRbrush_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtAdjustPrivilegesToken_arg3_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtAdjustPrivilegesToken_arg3_struct1(ctypes.Structure):
     _fields_ = (("reserve0", NtAdjustPrivilegesToken_arg3_struct2),
                 ("reserve1", ULONG)
                )

class NtAdjustPrivilegesToken_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtAdjustPrivilegesToken_arg3_struct1*341)
                )
class NtAdjustPrivilegesToken_arg5_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtAdjustPrivilegesToken_arg5_struct1(ctypes.Structure):
     _fields_ = (("reserve0", NtAdjustPrivilegesToken_arg5_struct2),
                 ("reserve1", ULONG)
                )

class NtAdjustPrivilegesToken_arg5_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtAdjustPrivilegesToken_arg5_struct1*341)
                )
class NtQueryInformationByName_arg1_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtQueryInformationByName_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtQueryInformationByName_arg1_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtQueryInformationByName_arg2_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtUserRedrawWindow_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct8(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct6(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct7(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct3(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct4),
                 ("reserve2", NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct5),
                 ("reserve3", NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct6),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", POINTER(NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct7)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG)
                )

class NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct2),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct3)
                )

class NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiDdDDICheckMultiPlaneOverlaySupport_arg1_struct8)
                )
class NtGdiDdDDIConfigureSharedResource_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", BYTE),
                 ("reserve3", ULONG),
                 ("reserve4", BYTE)
                ]
class NtOpenObjectAuditAlarm_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtOpenObjectAuditAlarm_arg3_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtOpenObjectAuditAlarm_arg4_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtOpenObjectAuditAlarm_arg5_struct2(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtOpenObjectAuditAlarm_arg5_struct1(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtOpenObjectAuditAlarm_arg5_struct2),
                 ("reserve3", ULONG*1024)
                ]

class NtOpenObjectAuditAlarm_arg5_struct4(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtOpenObjectAuditAlarm_arg5_struct3(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtOpenObjectAuditAlarm_arg5_struct4),
                 ("reserve3", ULONG*1024)
                ]

class NtOpenObjectAuditAlarm_arg5_struct5(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtOpenObjectAuditAlarm_arg5_struct6(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtOpenObjectAuditAlarm_arg5_struct0(ctypes.Structure):
     _fields_ = (("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", POINTER(NtOpenObjectAuditAlarm_arg5_struct1)),
                 ("reserve4", POINTER(NtOpenObjectAuditAlarm_arg5_struct3)),
                 ("reserve5", POINTER(NtOpenObjectAuditAlarm_arg5_struct5)),
                 ("reserve6", POINTER(NtOpenObjectAuditAlarm_arg5_struct6))
                )
class NtOpenObjectAuditAlarm_arg9_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtOpenObjectAuditAlarm_arg9_struct1(ctypes.Structure):
     _fields_ = (("reserve0", NtOpenObjectAuditAlarm_arg9_struct2),
                 ("reserve1", ULONG)
                )

class NtOpenObjectAuditAlarm_arg9_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtOpenObjectAuditAlarm_arg9_struct1*341)
                )
class NtGdiGetGlyphOutline_arg4_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiGetGlyphOutline_arg4_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiGetGlyphOutline_arg4_struct1),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                )
class NtGdiGetGlyphOutline_arg7_struct4(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT)
                ]

class NtGdiGetGlyphOutline_arg7_struct3(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT)
                ]

class NtGdiGetGlyphOutline_arg7_struct2(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT)
                ]

class NtGdiGetGlyphOutline_arg7_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT)
                ]

class NtGdiGetGlyphOutline_arg7_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiGetGlyphOutline_arg7_struct1),
                 ("reserve1", NtGdiGetGlyphOutline_arg7_struct2),
                 ("reserve2", NtGdiGetGlyphOutline_arg7_struct3),
                 ("reserve3", NtGdiGetGlyphOutline_arg7_struct4)
                )
class NtGdiDdDDILock2_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDILock2_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiDdDDILock2_arg1_struct1),
                 ("reserve3", POINTER(ULONG))
                ]
class NtGdiEngTextOut_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngTextOut_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngTextOut_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngTextOut_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngTextOut_arg2_struct6(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngTextOut_arg2_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngTextOut_arg2_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngTextOut_arg2_struct3(Structure):
     _fields_ = [("reserve0", NtGdiEngTextOut_arg2_struct4),
                 ("reserve1", NtGdiEngTextOut_arg2_struct5),
                 ("reserve2", BYTE*1)
                ]

class NtGdiEngTextOut_arg2_struct2(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", LPVOID),
                 ("reserve2", NtGdiEngTextOut_arg2_struct6)
                )

class NtGdiEngTextOut_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiEngTextOut_arg2_struct1),
                 ("reserve4", POINTER(NtGdiEngTextOut_arg2_struct2)),
                 ("reserve5", c_char_p)
                ]
class NtGdiEngTextOut_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngTextOut_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", NtGdiEngTextOut_arg3_struct1),
                 ("reserve7", ULONG),
                 ("reserve8", POINTER(ULONG)),
                 ("reserve9", POINTER(ULONG))
                ]
class NtGdiEngTextOut_arg4_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngTextOut_arg4_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiEngTextOut_arg4_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtGdiEngTextOut_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiEngTextOut_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiEngTextOut_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtGdiEngTextOut_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtGdiEngTextOut_arg9_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtAccessCheckByTypeAndAuditAlarm_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtAccessCheckByTypeAndAuditAlarm_arg3_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtAccessCheckByTypeAndAuditAlarm_arg4_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtAccessCheckByTypeAndAuditAlarm_arg5_struct2(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckByTypeAndAuditAlarm_arg5_struct1(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckByTypeAndAuditAlarm_arg5_struct2),
                 ("reserve3", ULONG*1024)
                ]

class NtAccessCheckByTypeAndAuditAlarm_arg5_struct4(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckByTypeAndAuditAlarm_arg5_struct3(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckByTypeAndAuditAlarm_arg5_struct4),
                 ("reserve3", ULONG*1024)
                ]

class NtAccessCheckByTypeAndAuditAlarm_arg5_struct5(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtAccessCheckByTypeAndAuditAlarm_arg5_struct6(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtAccessCheckByTypeAndAuditAlarm_arg5_struct0(ctypes.Structure):
     _fields_ = (("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", POINTER(NtAccessCheckByTypeAndAuditAlarm_arg5_struct1)),
                 ("reserve4", POINTER(NtAccessCheckByTypeAndAuditAlarm_arg5_struct3)),
                 ("reserve5", POINTER(NtAccessCheckByTypeAndAuditAlarm_arg5_struct5)),
                 ("reserve6", POINTER(NtAccessCheckByTypeAndAuditAlarm_arg5_struct6))
                )
class NtAccessCheckByTypeAndAuditAlarm_arg6_struct1(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckByTypeAndAuditAlarm_arg6_struct0(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckByTypeAndAuditAlarm_arg6_struct1),
                 ("reserve3", ULONG*1024)
                ]
class NtAccessCheckByTypeAndAuditAlarm_arg10_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]

class NtAccessCheckByTypeAndAuditAlarm_arg10_struct0(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtAccessCheckByTypeAndAuditAlarm_arg10_struct1))
                )
class NtAccessCheckByTypeAndAuditAlarm_arg12_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiGetRgnBox_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiDdDDICreateContext_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDICreateContext_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDICreateContext_arg1_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]

class NtGdiDdDDICreateContext_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiDdDDICreateContext_arg1_struct1),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", POINTER(ULONG)),
                 ("reserve9", ULONG),
                 ("reserve10", POINTER(NtGdiDdDDICreateContext_arg1_struct2)),
                 ("reserve11", ULONG),
                 ("reserve12", POINTER(NtGdiDdDDICreateContext_arg1_struct3)),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG)
                )
class NtGdiDdDDICreateContextVirtual_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDICreateContextVirtual_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiDdDDICreateContextVirtual_arg1_struct1),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG)
                ]
class NtReplacePartitionUnit_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtReplacePartitionUnit_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGdiSTROBJ_bEnumPositionsOnly_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiSTROBJ_bEnumPositionsOnly_arg1_struct6(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiSTROBJ_bEnumPositionsOnly_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiSTROBJ_bEnumPositionsOnly_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiSTROBJ_bEnumPositionsOnly_arg1_struct3(Structure):
     _fields_ = [("reserve0", NtGdiSTROBJ_bEnumPositionsOnly_arg1_struct4),
                 ("reserve1", NtGdiSTROBJ_bEnumPositionsOnly_arg1_struct5),
                 ("reserve2", BYTE*1)
                ]

class NtGdiSTROBJ_bEnumPositionsOnly_arg1_struct2(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", LPVOID),
                 ("reserve2", NtGdiSTROBJ_bEnumPositionsOnly_arg1_struct6)
                )

class NtGdiSTROBJ_bEnumPositionsOnly_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiSTROBJ_bEnumPositionsOnly_arg1_struct1),
                 ("reserve4", POINTER(NtGdiSTROBJ_bEnumPositionsOnly_arg1_struct2)),
                 ("reserve5", c_char_p)
                ]
class NtGdiDdDDIPresent_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]

class NtGdiDdDDIPresent_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIPresent_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIPresent_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIPresent_arg1_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIPresent_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", NtGdiDdDDIPresent_arg1_struct1),
                 ("reserve7", NtGdiDdDDIPresent_arg1_struct2),
                 ("reserve8", ULONG),
                 ("reserve9", POINTER(NtGdiDdDDIPresent_arg1_struct3)),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", NtGdiDdDDIPresent_arg1_struct4),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG*64),
                 ("reserve15", ULONG),
                 ("reserve16", NtGdiDdDDIPresent_arg1_struct5)
                )
class NtUserGetScrollBarInfo_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtUserGetScrollBarInfo_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", NtUserGetScrollBarInfo_arg3_struct1),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]
class NtGdiFONTOBJ_pfdg_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiFONTOBJ_pfdg_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", NtGdiFONTOBJ_pfdg_arg1_struct1),
                 ("reserve7", ULONG),
                 ("reserve8", POINTER(ULONG)),
                 ("reserve9", POINTER(ULONG))
                ]
class NtGdiDdDDIEnumAdapters_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDIEnumAdapters_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDIEnumAdapters_arg1_struct2),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                )

class NtGdiDdDDIEnumAdapters_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDIEnumAdapters_arg1_struct1*16)
                )
class NtGdiGetFontUnicodeRanges_arg2_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT)
                ]

class NtGdiGetFontUnicodeRanges_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiGetFontUnicodeRanges_arg2_struct1*1)
                )
class NtUnsubscribeWnfStateChange_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtUnsubscribeWnfStateChange_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtUnsubscribeWnfStateChange_arg1_struct6(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtUnsubscribeWnfStateChange_arg1_struct7(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtUnsubscribeWnfStateChange_arg1_struct3(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", POINTER(NtUnsubscribeWnfStateChange_arg1_struct4)),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", POINTER(ULONG)),
                 ("reserve17", POINTER(NtUnsubscribeWnfStateChange_arg1_struct5)),
                 ("reserve18", POINTER(NtUnsubscribeWnfStateChange_arg1_struct6)),
                 ("reserve19", ULONG),
                 ("reserve20", c_longlong),
                 ("reserve21", ULONG),
                 ("reserve22", POINTER(NtUnsubscribeWnfStateChange_arg1_struct7)),
                 ("reserve23", ULONG),
                 ("reserve24", BYTE),
                 ("reserve25", ULONG)
                )

class NtUnsubscribeWnfStateChange_arg1_struct2(Structure):
     _fields_ = [("reserve0", POINTER(NtUnsubscribeWnfStateChange_arg1_struct3)),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]

class NtUnsubscribeWnfStateChange_arg1_struct8(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                ]

class NtUnsubscribeWnfStateChange_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(NtUnsubscribeWnfStateChange_arg1_struct2)),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", POINTER(NtUnsubscribeWnfStateChange_arg1_struct8)),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG),
                 ("reserve23", ULONG),
                 ("reserve24", ULONG)
                )

class NtUnsubscribeWnfStateChange_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", POINTER(NtUnsubscribeWnfStateChange_arg1_struct1)),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG),
                 ("reserve23", ULONG)
                )
class NtUserInitializeClientPfnArrays_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserInitializeClientPfnArrays_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserInitializeClientPfnArrays_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiGetBitmapDimension_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiBRUSHOBJ_ulGetBrushColor_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtGdiEngFillPath_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngFillPath_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngFillPath_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngFillPath_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiEngFillPath_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngFillPath_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiEngFillPath_arg3_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtGdiEngFillPath_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtGdiEngFillPath_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtCreateKeyTransacted_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtCreateKeyTransacted_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateKeyTransacted_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtCreateKeyTransacted_arg5_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGdiDdDDISubmitCommandToHwQueue_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", LPVOID),
                 ("reserve6", ULONG),
                 ("reserve7", LPVOID)
                ]
class NtUserCalculatePopupWindowPosition_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserCalculatePopupWindowPosition_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserCalculatePopupWindowPosition_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUserCalculatePopupWindowPosition_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtCreateTransactionManager_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtCreateTransactionManager_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateTransactionManager_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtCreateTransactionManager_arg4_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserGetPointerInputTransform_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG*4),
                 ("reserve1", ULONG*4),
                 ("reserve2", ULONG*4),
                 ("reserve3", ULONG*4)
                ]

class NtUserGetPointerInputTransform_arg3_struct0(Structure):
     _fields_ = [("reserve0", NtUserGetPointerInputTransform_arg3_struct1)
                ]
class NtUserGetGUIThreadInfo_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtUserGetGUIThreadInfo_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", NtUserGetGUIThreadInfo_arg2_struct1)
                )
class NtUserGetTitleBarInfo_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtUserGetTitleBarInfo_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", NtUserGetTitleBarInfo_arg2_struct1)
                ]
class NtGdiDdDDIReserveGpuVirtualAddress_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG)
                ]
class NtDeleteWnfStateName_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtCreateTimer_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtCreateTimer_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateTimer_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiDdDDIEscape_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIEscape_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIEscape_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiDdDDIEscape_arg1_struct1),
                 ("reserve4", POINTER(NtGdiDdDDIEscape_arg1_struct2)),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                )
class NtOpenSymbolicLinkObject_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenSymbolicLinkObject_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenSymbolicLinkObject_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtUserRegisterUserApiHook_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserRegisterUserApiHook_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtCreatePrivateNamespace_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreatePrivateNamespace_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]
class NtGdiEngGradientFill_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngGradientFill_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngGradientFill_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngGradientFill_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngGradientFill_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiEngGradientFill_arg2_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtGdiEngGradientFill_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiEngGradientFill_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", USHORT)
                ]
class NtGdiEngGradientFill_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiEngGradientFill_arg9_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDISetDisplayPrivateDriverFormat_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtGdiDdDDIMapGpuVirtualAddress_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIMapGpuVirtualAddress_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", NtGdiDdDDIMapGpuVirtualAddress_arg1_struct1),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG)
                )
class NtGdiDdDDIOpenProtectedSessionFromNtHandle_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtQueryAttributesFile_arg1_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtQueryAttributesFile_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", c_char_p),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", USHORT)
                )
class NtQueryAttributesFile_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiRemoveFontResourceW_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG*16)
                ]
class NtSubscribeWnfStateChange_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtSubscribeWnfStateChange_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtSubscribeWnfStateChange_arg1_struct6(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtSubscribeWnfStateChange_arg1_struct7(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtSubscribeWnfStateChange_arg1_struct3(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", POINTER(NtSubscribeWnfStateChange_arg1_struct4)),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", POINTER(ULONG)),
                 ("reserve17", POINTER(NtSubscribeWnfStateChange_arg1_struct5)),
                 ("reserve18", POINTER(NtSubscribeWnfStateChange_arg1_struct6)),
                 ("reserve19", ULONG),
                 ("reserve20", c_longlong),
                 ("reserve21", ULONG),
                 ("reserve22", POINTER(NtSubscribeWnfStateChange_arg1_struct7)),
                 ("reserve23", ULONG),
                 ("reserve24", BYTE),
                 ("reserve25", ULONG)
                )

class NtSubscribeWnfStateChange_arg1_struct2(Structure):
     _fields_ = [("reserve0", POINTER(NtSubscribeWnfStateChange_arg1_struct3)),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]

class NtSubscribeWnfStateChange_arg1_struct8(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                ]

class NtSubscribeWnfStateChange_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(NtSubscribeWnfStateChange_arg1_struct2)),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", POINTER(NtSubscribeWnfStateChange_arg1_struct8)),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG),
                 ("reserve23", ULONG),
                 ("reserve24", ULONG)
                )

class NtSubscribeWnfStateChange_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", POINTER(NtSubscribeWnfStateChange_arg1_struct1)),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG),
                 ("reserve23", ULONG)
                )
class NtSubscribeWnfStateChange_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDIReclaimAllocations2_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", POINTER(ULONG)),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", ULONG)
                ]
class NtCreateSemaphore_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateSemaphore_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtCreateSemaphore_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateSemaphore_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", USHORT),
                 ("reserve7", USHORT),
                 ("reserve8", c_char_p)
                ]
class NtGdiScaleWindowExtEx_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtMapViewOfSectionEx_arg8_struct0(Structure):
     _fields_ = [("reserve0", c_longlong),
                 ("reserve1", c_longlong)
                ]
class NtUserEndPaint_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetCIMSSM_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserTestForInteractiveUser_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateSymbolicLinkObject_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateSymbolicLinkObject_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtCreateSymbolicLinkObject_arg3_struct4(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtCreateSymbolicLinkObject_arg3_struct3(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtCreateSymbolicLinkObject_arg3_struct4),
                 ("reserve3", ULONG*1024)
                ]

class NtCreateSymbolicLinkObject_arg3_struct6(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtCreateSymbolicLinkObject_arg3_struct5(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtCreateSymbolicLinkObject_arg3_struct6),
                 ("reserve3", ULONG*1024)
                ]

class NtCreateSymbolicLinkObject_arg3_struct7(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtCreateSymbolicLinkObject_arg3_struct8(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtCreateSymbolicLinkObject_arg3_struct2(ctypes.Structure):
     _fields_ = (("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", POINTER(NtCreateSymbolicLinkObject_arg3_struct3)),
                 ("reserve4", POINTER(NtCreateSymbolicLinkObject_arg3_struct5)),
                 ("reserve5", POINTER(NtCreateSymbolicLinkObject_arg3_struct7)),
                 ("reserve6", POINTER(NtCreateSymbolicLinkObject_arg3_struct8))
                )

class NtCreateSymbolicLinkObject_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateSymbolicLinkObject_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(NtCreateSymbolicLinkObject_arg3_struct2)),
                 ("reserve5", ULONG)
                )
class NtCreateSymbolicLinkObject_arg4_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserUpdateLayeredWindow_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserUpdateLayeredWindow_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserUpdateLayeredWindow_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserUpdateLayeredWindow_arg8_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", BYTE),
                 ("reserve2", BYTE)
                ]
class NtGdiDdDDIGetSharedResourceAdapterLuid_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDIGetSharedResourceAdapterLuid_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiDdDDIGetSharedResourceAdapterLuid_arg1_struct1)
                )
class NtGdiFONTOBJ_vGetInfo_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiFONTOBJ_vGetInfo_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", NtGdiFONTOBJ_vGetInfo_arg1_struct1),
                 ("reserve7", ULONG),
                 ("reserve8", POINTER(ULONG)),
                 ("reserve9", POINTER(ULONG))
                ]
class NtGdiFONTOBJ_vGetInfo_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                ]
class NtUserInjectPointerInput_arg2_struct8(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtUserInjectPointerInput_arg2_struct7(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtUserInjectPointerInput_arg2_struct6(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserInjectPointerInput_arg2_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserInjectPointerInput_arg2_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserInjectPointerInput_arg2_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserInjectPointerInput_arg2_struct2(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", NtUserInjectPointerInput_arg2_struct3),
                 ("reserve7", NtUserInjectPointerInput_arg2_struct4),
                 ("reserve8", NtUserInjectPointerInput_arg2_struct5),
                 ("reserve9", NtUserInjectPointerInput_arg2_struct6),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG)
                )

class NtUserInjectPointerInput_arg2_struct1(ctypes.Structure):
     _fields_ = (("reserve0", NtUserInjectPointerInput_arg2_struct2),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtUserInjectPointerInput_arg2_struct7),
                 ("reserve4", NtUserInjectPointerInput_arg2_struct8),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                )

class NtUserInjectPointerInput_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtUserInjectPointerInput_arg2_struct1)
                )
class NtGdiCreateColorSpace_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]

class NtGdiCreateColorSpace_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]

class NtGdiCreateColorSpace_arg1_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]

class NtGdiCreateColorSpace_arg1_struct2(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiCreateColorSpace_arg1_struct3),
                 ("reserve1", NtGdiCreateColorSpace_arg1_struct4),
                 ("reserve2", NtGdiCreateColorSpace_arg1_struct5)
                )

class NtGdiCreateColorSpace_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", NtGdiCreateColorSpace_arg1_struct2),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", c_char*2048)
                )

class NtGdiCreateColorSpace_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiCreateColorSpace_arg1_struct1),
                 ("reserve1", ULONG)
                )
class NtGdiDdDDIFlushHeapTransitions_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtOpenKeyEx_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenKeyEx_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenKeyEx_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtUserCallMsgFilter_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserCallMsgFilter_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", BYTE),
                 ("reserve3", POINTER(ULONG)),
                 ("reserve4", ULONG),
                 ("reserve5", NtUserCallMsgFilter_arg1_struct1),
                 ("reserve6", ULONG)
                )
class NtLoadDriver_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserTransformPoint_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtEnumerateTransactionObject_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]

class NtEnumerateTransactionObject_arg3_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]

class NtEnumerateTransactionObject_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtEnumerateTransactionObject_arg3_struct1),
                 ("reserve1", ULONG),
                 ("reserve2", NtEnumerateTransactionObject_arg3_struct2*1)
                )
class NtUserPerMonitorDPIPhysicalToLogicalPoint_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtSetCachedSigningLevel_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDISubmitWaitForSyncObjectsToHwQueue_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", LPVOID),
                 ("reserve3", LPVOID)
                ]
class NtQueryVolumeInformationFile_arg2_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDIWaitForSynchronizationObjectFromCpu_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIWaitForSynchronizationObjectFromCpu_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", LPVOID),
                 ("reserve3", LPVOID),
                 ("reserve4", ULONG),
                 ("reserve5", NtGdiDdDDIWaitForSynchronizationObjectFromCpu_arg1_struct1)
                )
class NtUserGetUpdateRect_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtQuerySecurityObject_arg3_struct2(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtQuerySecurityObject_arg3_struct1(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtQuerySecurityObject_arg3_struct2),
                 ("reserve3", ULONG*1024)
                ]

class NtQuerySecurityObject_arg3_struct4(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtQuerySecurityObject_arg3_struct3(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtQuerySecurityObject_arg3_struct4),
                 ("reserve3", ULONG*1024)
                ]

class NtQuerySecurityObject_arg3_struct5(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtQuerySecurityObject_arg3_struct6(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtQuerySecurityObject_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", POINTER(NtQuerySecurityObject_arg3_struct1)),
                 ("reserve4", POINTER(NtQuerySecurityObject_arg3_struct3)),
                 ("reserve5", POINTER(NtQuerySecurityObject_arg3_struct5)),
                 ("reserve6", POINTER(NtQuerySecurityObject_arg3_struct6))
                )
class NtSetSecurityObject_arg3_struct2(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtSetSecurityObject_arg3_struct1(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtSetSecurityObject_arg3_struct2),
                 ("reserve3", ULONG*1024)
                ]

class NtSetSecurityObject_arg3_struct4(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtSetSecurityObject_arg3_struct3(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtSetSecurityObject_arg3_struct4),
                 ("reserve3", ULONG*1024)
                ]

class NtSetSecurityObject_arg3_struct5(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtSetSecurityObject_arg3_struct6(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtSetSecurityObject_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", POINTER(NtSetSecurityObject_arg3_struct1)),
                 ("reserve4", POINTER(NtSetSecurityObject_arg3_struct3)),
                 ("reserve5", POINTER(NtSetSecurityObject_arg3_struct5)),
                 ("reserve6", POINTER(NtSetSecurityObject_arg3_struct6))
                )
class NtGdiDdDDISharedPrimaryLockNotification_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDISharedPrimaryLockNotification_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDISharedPrimaryLockNotification_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiDdDDISharedPrimaryLockNotification_arg1_struct1),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiDdDDISharedPrimaryLockNotification_arg1_struct2)
                )
class NtOpenSemaphore_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtOpenSemaphore_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenSemaphore_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenSemaphore_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", USHORT),
                 ("reserve7", USHORT),
                 ("reserve8", c_char_p)
                ]
class NtGdiDdDDICreatePagingQueue_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", ULONG)
                ]
class NtGdiDdDDIUpdateOverlay_arg1_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIUpdateOverlay_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIUpdateOverlay_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDIUpdateOverlay_arg1_struct2),
                 ("reserve2", NtGdiDdDDIUpdateOverlay_arg1_struct3),
                 ("reserve3", POINTER(ULONG)),
                 ("reserve4", ULONG)
                ]

class NtGdiDdDDIUpdateOverlay_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiDdDDIUpdateOverlay_arg1_struct1)
                )
class NtUserRegisterClassExWOW_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", c_char_p),
                 ("reserve10", c_char_p),
                 ("reserve11", ULONG)
                ]
class NtUserRegisterClassExWOW_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserRegisterClassExWOW_arg3_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserRegisterClassExWOW_arg4_struct0(Structure):
     _fields_ = [("reserve0", c_char_p)
                ]
class NtGdiDdDDICreateHwQueue_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDICreateHwQueue_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDICreateHwQueue_arg1_struct1),
                 ("reserve2", ULONG),
                 ("reserve3", LPVOID),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", POINTER(ULONG)),
                 ("reserve7", ULONG)
                ]
class NtGdiPATHOBJ_vEnumStart_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDICheckOcclusion_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDICreateKeyedMutex_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtCreateJobSet_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtGdiIcmBrushInfo_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG)
                ]

class NtGdiIcmBrushInfo_arg3_struct0(Structure):
     _fields_ = [("reserve0", NtGdiIcmBrushInfo_arg3_struct1),
                 ("reserve1", ULONG*1)
                ]
class NtOpenSection_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenSection_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenSection_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtAssociateWaitCompletionPacket_arg1_struct0(Structure):
     _fields_ = [("reserve0", BYTE)
                ]
class NtAssociateWaitCompletionPacket_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", c_longlong*2),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT),
                 ("reserve13", c_longlong*2),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG)
                ]
class NtAssociateWaitCompletionPacket_arg5_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", c_longlong*2),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG)
                ]
class NtAssociateWaitCompletionPacket_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiGetPath_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserGetIconSize_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetIconSize_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserDrawIconEx_arg11_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                ]
class NtGdiDdDDICreateAllocation_arg1_struct3(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDICreateAllocation_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDICreateAllocation_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDICreateAllocation_arg1_struct2),
                 ("reserve2", NtGdiDdDDICreateAllocation_arg1_struct3)
                )

class NtGdiDdDDICreateAllocation_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]

class NtGdiDdDDICreateAllocation_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", LPVOID),
                 ("reserve4", ULONG),
                 ("reserve5", POINTER(NtGdiDdDDICreateAllocation_arg1_struct1)),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", LPVOID),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG)
                )
class NtUpdateWnfStateData_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUpdateWnfStateData_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", USHORT),
                 ("reserve6", BYTE*8),
                 ("reserve7", USHORT),
                 ("reserve8", BYTE*8),
                 ("reserve9", USHORT),
                 ("reserve10", ULONG)
                ]
class NtOpenEnlistment_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]
class NtOpenEnlistment_arg5_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenEnlistment_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenEnlistment_arg5_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiGetAppClipBox_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtQueryInformationWorkerFactory_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtReadFileScatter_arg5_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtReadFileScatter_arg5_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtReadFileScatter_arg5_struct1),
                 ("reserve3", ULONG)
                )
class NtReadFileScatter_arg8_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtReadFileScatter_arg8_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtReadFileScatter_arg8_struct1),
                 ("reserve1", ULONG)
                )
class NtOpenTimer_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenTimer_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenTimer_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtUserLogicalToPhysicalPoint_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtQueryDirectoryFileEx_arg5_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtQueryDirectoryFileEx_arg10_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGdiEngStrokePath_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngStrokePath_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngStrokePath_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngStrokePath_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiEngStrokePath_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngStrokePath_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiEngStrokePath_arg3_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtGdiEngStrokePath_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiEngStrokePath_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtGdiEngStrokePath_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiEngStrokePath_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", POINTER(ULONG)),
                 ("reserve7", ULONG)
                ]
class NtUnloadDriver_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtRIMGetPhysicalDeviceRect_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiPATHOBJ_bEnumClipLines_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiPATHOBJ_bEnumClipLines_arg3_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiPATHOBJ_bEnumClipLines_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiPATHOBJ_bEnumClipLines_arg3_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiPATHOBJ_bEnumClipLines_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiPATHOBJ_bEnumClipLines_arg3_struct1),
                 ("reserve1", NtGdiPATHOBJ_bEnumClipLines_arg3_struct2),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiPATHOBJ_bEnumClipLines_arg3_struct3*1)
                )
class NtQuerySection_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtRenameTransactionManager_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtRenameTransactionManager_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]
class NtGdiDdDDICreateOverlay_arg1_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDICreateOverlay_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDICreateOverlay_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDICreateOverlay_arg1_struct2),
                 ("reserve2", NtGdiDdDDICreateOverlay_arg1_struct3),
                 ("reserve3", POINTER(ULONG)),
                 ("reserve4", ULONG)
                ]

class NtGdiDdDDICreateOverlay_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiDdDDICreateOverlay_arg1_struct1),
                 ("reserve3", ULONG)
                )
class NtRaiseHardError_arg4_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtRaiseHardError_arg4_struct0(Structure):
     _fields_ = [("reserve0", POINTER(NtRaiseHardError_arg4_struct1))
                ]
class NtRaiseHardError_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtQuerySystemEnvironmentValueEx_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtQuerySystemEnvironmentValueEx_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", BYTE*8)
                ]
class NtQuerySystemEnvironmentValueEx_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIGetPresentHistory_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", LPVOID),
                 ("reserve4", ULONG)
                ]
class NtUserGetPointerDevice_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", USHORT),
                 ("reserve6", c_char*2048)
                ]
class NtCreateIoCompletion_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtUserFindExistingCursorIcon_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserFindExistingCursorIcon_arg2_struct1(Structure):
     _fields_ = [("reserve0", c_char*2048)
                ]

class NtUserFindExistingCursorIcon_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtUserFindExistingCursorIcon_arg2_struct1))
                )
class NtUserFindExistingCursorIcon_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", BYTE),
                 ("reserve6", BYTE)
                ]
class NtOpenFile_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenFile_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenFile_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtOpenFile_arg4_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtFlushVirtualMemory_arg4_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtUserGetAltTabInfo_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserGetAltTabInfo_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", NtUserGetAltTabInfo_arg3_struct1)
                )
class NtUserEnumDisplayMonitors_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiDdDDIQueryResourceInfo_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                ]
class NtGdiEngEraseSurface_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngEraseSurface_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngEraseSurface_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngEraseSurface_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiDdDDIGetMultisampleMethodList_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]

class NtGdiDdDDIGetMultisampleMethodList_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", POINTER(NtGdiDdDDIGetMultisampleMethodList_arg1_struct1)),
                 ("reserve6", ULONG)
                )
class NtGdiDdDDILock_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDILock_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG)),
                 ("reserve6", NtGdiDdDDILock_arg1_struct1),
                 ("reserve7", ULONG)
                )
class NtGdiDdDDIEnumAdapters2_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDIEnumAdapters2_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDIEnumAdapters2_arg1_struct2),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                )

class NtGdiDdDDIEnumAdapters2_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", POINTER(NtGdiDdDDIEnumAdapters2_arg1_struct1))
                )
class NtSetTimer2_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtSetTimer2_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIChangeVideoMemoryReservation_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG)
                ]
class NtGdiSTROBJ_bEnum_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiSTROBJ_bEnum_arg1_struct6(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiSTROBJ_bEnum_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiSTROBJ_bEnum_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiSTROBJ_bEnum_arg1_struct3(Structure):
     _fields_ = [("reserve0", NtGdiSTROBJ_bEnum_arg1_struct4),
                 ("reserve1", NtGdiSTROBJ_bEnum_arg1_struct5),
                 ("reserve2", BYTE*1)
                ]

class NtGdiSTROBJ_bEnum_arg1_struct2(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", LPVOID),
                 ("reserve2", NtGdiSTROBJ_bEnum_arg1_struct6)
                )

class NtGdiSTROBJ_bEnum_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiSTROBJ_bEnum_arg1_struct1),
                 ("reserve4", POINTER(NtGdiSTROBJ_bEnum_arg1_struct2)),
                 ("reserve5", c_char_p)
                ]
class NtGdiDdDDISetVidPnSourceOwner_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDISetVidPnSourceOwner_arg1_struct0(Structure):
     _fields_ = [("reserve0", NtGdiDdDDISetVidPnSourceOwner_arg1_struct1),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG))
                ]
class NtRegisterProtocolAddressInformation_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]
class NtGetNotificationResourceManager_arg2_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG),
                 ("reserve2", c_longlong),
                 ("reserve3", ULONG)
                ]
class NtSetEaFile_arg2_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtGdiFONTOBJ_cGetGlyphs_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiFONTOBJ_cGetGlyphs_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", NtGdiFONTOBJ_cGetGlyphs_arg1_struct1),
                 ("reserve7", ULONG),
                 ("reserve8", POINTER(ULONG)),
                 ("reserve9", POINTER(ULONG))
                ]
class NtUserGetCaretPos_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDIQueryAdapterInfo_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", ULONG)
                ]
class NtUserGetMessage_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserGetMessage_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", POINTER(ULONG)),
                 ("reserve4", ULONG),
                 ("reserve5", NtUserGetMessage_arg1_struct1),
                 ("reserve6", ULONG)
                )
class NtCreateWorkerFactory_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtCreateWorkerFactory_arg7_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtCreateWorkerFactory_arg7_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]

class NtCreateWorkerFactory_arg7_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", ULONG),
                 ("reserve3", POINTER(NtCreateWorkerFactory_arg7_struct1)),
                 ("reserve4", POINTER(NtCreateWorkerFactory_arg7_struct2)),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                )
class NtGdiDdDDIDestroyHwContext_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiTransformPoints_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiTransformPoints_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtQueryValueKey_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGdiXFORMOBJ_bApplyXform_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiXFORMOBJ_bApplyXform_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiXFORMOBJ_bApplyXform_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDISubmitSignalSyncObjectsToHwQueue_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDISubmitSignalSyncObjectsToHwQueue_arg1_struct0(Structure):
     _fields_ = [("reserve0", NtGdiDdDDISubmitSignalSyncObjectsToHwQueue_arg1_struct1),
                 ("reserve1", ULONG),
                 ("reserve2", LPVOID),
                 ("reserve3", ULONG),
                 ("reserve4", LPVOID),
                 ("reserve5", LPVOID)
                ]
class NtGdiMoveTo_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtSetValueKey_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGdiOpenDCW_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGdiOpenDCW_arg2_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT)
                ]

class NtGdiOpenDCW_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", c_char*64),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", ULONG),
                 ("reserve6", NtGdiOpenDCW_arg2_struct1),
                 ("reserve7", USHORT),
                 ("reserve8", USHORT),
                 ("reserve9", USHORT),
                 ("reserve10", USHORT),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT),
                 ("reserve13", USHORT),
                 ("reserve14", USHORT),
                 ("reserve15", USHORT),
                 ("reserve16", c_char*64),
                 ("reserve17", USHORT),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG),
                 ("reserve23", ULONG),
                 ("reserve24", ULONG),
                 ("reserve25", ULONG),
                 ("reserve26", ULONG),
                 ("reserve27", ULONG),
                 ("reserve28", ULONG),
                 ("reserve29", ULONG),
                 ("reserve30", ULONG)
                )
class NtGdiOpenDCW_arg3_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGdiOpenDCW_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", c_char_p),
                 ("reserve2", c_char_p),
                 ("reserve3", c_char_p),
                 ("reserve4", c_char_p),
                 ("reserve5", c_char_p)
                ]
class NtGdiDdDDIQueryProcessOfferInfo_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiGetUFI_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG*16)
                ]
class NtRequestWaitReplyPort_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG)
                ]
class NtRequestWaitReplyPort_arg3_struct0(Structure):
     _fields_ = [("reserve0", c_longlong*2)
                ]
class NtGdiDdDDIOutputDuplGetMetaData_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", LPVOID),
                 ("reserve5", ULONG)
                ]
class NtGdiDdDDIUnlock2_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDISetContextSchedulingPriority_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtQueryInstallUILanguage_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT)
                ]
class NtGdiDdDDISignalSynchronizationObject_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDISignalSynchronizationObject_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG*32),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG),
                 ("reserve23", ULONG),
                 ("reserve24", ULONG),
                 ("reserve25", ULONG),
                 ("reserve26", ULONG),
                 ("reserve27", ULONG),
                 ("reserve28", ULONG),
                 ("reserve29", ULONG),
                 ("reserve30", ULONG),
                 ("reserve31", ULONG),
                 ("reserve32", ULONG),
                 ("reserve33", ULONG),
                 ("reserve34", NtGdiDdDDISignalSynchronizationObject_arg1_struct1),
                 ("reserve35", ULONG),
                 ("reserve36", ULONG*64),
                 ("reserve37", ULONG),
                 ("reserve38", ULONG),
                 ("reserve39", ULONG),
                 ("reserve40", ULONG),
                 ("reserve41", ULONG),
                 ("reserve42", ULONG),
                 ("reserve43", ULONG),
                 ("reserve44", ULONG),
                 ("reserve45", ULONG),
                 ("reserve46", ULONG),
                 ("reserve47", ULONG),
                 ("reserve48", ULONG),
                 ("reserve49", ULONG),
                 ("reserve50", ULONG),
                 ("reserve51", ULONG),
                 ("reserve52", ULONG),
                 ("reserve53", ULONG),
                 ("reserve54", ULONG),
                 ("reserve55", ULONG),
                 ("reserve56", ULONG),
                 ("reserve57", ULONG),
                 ("reserve58", ULONG),
                 ("reserve59", ULONG),
                 ("reserve60", ULONG),
                 ("reserve61", ULONG),
                 ("reserve62", ULONG),
                 ("reserve63", ULONG),
                 ("reserve64", ULONG),
                 ("reserve65", ULONG),
                 ("reserve66", ULONG),
                 ("reserve67", ULONG),
                 ("reserve68", ULONG),
                 ("reserve69", ULONG),
                 ("reserve70", ULONG),
                 ("reserve71", ULONG),
                 ("reserve72", ULONG),
                 ("reserve73", ULONG),
                 ("reserve74", ULONG),
                 ("reserve75", ULONG),
                 ("reserve76", ULONG),
                 ("reserve77", ULONG),
                 ("reserve78", ULONG),
                 ("reserve79", ULONG),
                 ("reserve80", ULONG),
                 ("reserve81", ULONG),
                 ("reserve82", ULONG),
                 ("reserve83", ULONG),
                 ("reserve84", ULONG),
                 ("reserve85", ULONG),
                 ("reserve86", ULONG),
                 ("reserve87", ULONG),
                 ("reserve88", ULONG),
                 ("reserve89", ULONG),
                 ("reserve90", ULONG),
                 ("reserve91", ULONG),
                 ("reserve92", ULONG),
                 ("reserve93", ULONG),
                 ("reserve94", ULONG),
                 ("reserve95", ULONG),
                 ("reserve96", ULONG),
                 ("reserve97", ULONG),
                 ("reserve98", ULONG),
                 ("reserve99", ULONG),
                 ("reserve100", c_longlong*8),
                 ("reserve101", ULONG),
                 ("reserve102", ULONG),
                 ("reserve103", ULONG),
                 ("reserve104", ULONG),
                 ("reserve105", ULONG),
                 ("reserve106", ULONG),
                 ("reserve107", ULONG),
                 ("reserve108", ULONG),
                 ("reserve109", ULONG),
                 ("reserve110", ULONG),
                 ("reserve111", ULONG),
                 ("reserve112", ULONG),
                 ("reserve113", ULONG),
                 ("reserve114", ULONG),
                 ("reserve115", ULONG)
                ]
class NtGdiEngUnlockSurface_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngUnlockSurface_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngUnlockSurface_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtQueryLicenseValue_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtQueryLicenseValue_arg2_struct0(Structure):
     _fields_ = [("reserve0", POINTER(c_longlong))
                ]
class NtQueryLicenseValue_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserSetCursorIconData_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserSetCursorIconData_arg3_struct1(Structure):
     _fields_ = [("reserve0", c_char*2048)
                ]

class NtUserSetCursorIconData_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtUserSetCursorIconData_arg3_struct1))
                )
class NtUserSetCursorIconData_arg4_struct1(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE)
                ]

class NtUserSetCursorIconData_arg4_struct2(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtUserSetCursorIconData_arg4_struct0(ctypes.Structure):
     _fields_ = (("reserve0", c_char_p),
                 ("reserve1", POINTER(NtUserSetCursorIconData_arg4_struct1)),
                 ("reserve2", USHORT),
                 ("reserve3", ULONG),
                 ("reserve4", USHORT),
                 ("reserve5", USHORT),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", BYTE),
                 ("reserve18", ULONG),
                 ("reserve19", POINTER(NtUserSetCursorIconData_arg4_struct2)),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG)
                )
class NtGdiCombineTransform_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]
class NtGdiCombineTransform_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]
class NtGdiCombineTransform_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]
class NtOpenKeyTransactedEx_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenKeyTransactedEx_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenKeyTransactedEx_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiCreatePaletteInternal_arg1_struct1(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE)
                ]

class NtGdiCreatePaletteInternal_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", NtGdiCreatePaletteInternal_arg1_struct1*1024)
                )
class NtSetVolumeInformationFile_arg2_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDIMakeResident_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIMakeResident_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", LPVOID),
                 ("reserve3", POINTER(ULONG)),
                 ("reserve4", NtGdiDdDDIMakeResident_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                )
class NtGdiDdDDIOpenAdapterFromLuid_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDIOpenAdapterFromLuid_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiDdDDIOpenAdapterFromLuid_arg1_struct1),
                 ("reserve1", ULONG)
                )
class NtGdiDdDDICloseAdapter_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtDebugContinue_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtQueryDirectoryObject_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtQueryDirectoryObject_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtTraceControl_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIGetMultiPlaneOverlayCaps_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIGetMultiPlaneOverlayCaps_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", NtGdiDdDDIGetMultiPlaneOverlayCaps_arg1_struct1),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG)
                )
class NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg4_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg5_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg6_struct2(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg6_struct1(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg6_struct2),
                 ("reserve3", ULONG*1024)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg6_struct4(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg6_struct3(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg6_struct4),
                 ("reserve3", ULONG*1024)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg6_struct5(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg6_struct6(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg6_struct0(ctypes.Structure):
     _fields_ = (("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", POINTER(NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg6_struct1)),
                 ("reserve4", POINTER(NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg6_struct3)),
                 ("reserve5", POINTER(NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg6_struct5)),
                 ("reserve6", POINTER(NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg6_struct6))
                )
class NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg7_struct1(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg7_struct0(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg7_struct1),
                 ("reserve3", ULONG*1024)
                ]
class NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg11_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg11_struct0(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg11_struct1))
                )
class NtAccessCheckByTypeResultListAndAuditAlarmByHandle_arg13_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtWriteFile_arg5_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtGdiEngAlphaBlend_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngAlphaBlend_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngAlphaBlend_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngAlphaBlend_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngAlphaBlend_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngAlphaBlend_arg2_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngAlphaBlend_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngAlphaBlend_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiEngAlphaBlend_arg3_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtGdiEngAlphaBlend_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiEngAlphaBlend_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiEngAlphaBlend_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiEngAlphaBlend_arg7_struct1(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE)
                ]

class NtGdiEngAlphaBlend_arg7_struct0(Structure):
     _fields_ = [("reserve0", NtGdiEngAlphaBlend_arg7_struct1)
                ]
class NtRIMRegisterForInput_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtRIMRegisterForInput_arg4_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT)
                ]
class NtGdiDdDDIQueryClockCalibration_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIQueryClockCalibration_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiDdDDIQueryClockCalibration_arg1_struct2)
                )

class NtGdiDdDDIQueryClockCalibration_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiDdDDIQueryClockCalibration_arg1_struct1)
                )
class NtGdiDdDDISetGammaRamp_arg1_struct1(Structure):
     _fields_ = [("reserve0", USHORT*256),
                 ("reserve1", USHORT*256),
                 ("reserve2", USHORT*256)
                ]

class NtGdiDdDDISetGammaRamp_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", POINTER(NtGdiDdDDISetGammaRamp_arg1_struct1)),
                 ("reserve4", ULONG)
                )
class NtGdiPATHOBJ_vEnumStartClipLines_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiPATHOBJ_vEnumStartClipLines_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiPATHOBJ_vEnumStartClipLines_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiPATHOBJ_vEnumStartClipLines_arg2_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtGdiPATHOBJ_vEnumStartClipLines_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiPATHOBJ_vEnumStartClipLines_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiPATHOBJ_vEnumStartClipLines_arg3_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiPATHOBJ_vEnumStartClipLines_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", POINTER(ULONG)),
                 ("reserve7", ULONG)
                ]
class NtRIMReadInput_arg7_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtUnlockVirtualMemory_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUnlockVirtualMemory_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtWaitForAlertByThreadId_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtWaitForAlertByThreadId_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtOpenProcess_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenProcess_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenProcess_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtOpenProcess_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDIWaitForIdle_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserInitializeInputDeviceInjection_arg3_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", USHORT),
                 ("reserve6", USHORT),
                 ("reserve7", BYTE),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG)
                ]
class NtGdiDdDDIOutputDuplReleaseFrame_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtLockFile_arg5_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDIGetDisplayModeList_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDIGetDisplayModeList_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiDdDDIGetDisplayModeList_arg1_struct2),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG)
                )

class NtGdiDdDDIGetDisplayModeList_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtGdiDdDDIGetDisplayModeList_arg1_struct1)),
                 ("reserve3", ULONG)
                )
class NtUserChangeWindowMessageFilterEx_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiRectInRegion_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiDdDDISetQueuedLimit_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDISetQueuedLimit_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiDdDDISetQueuedLimit_arg1_struct1)
                )
class NtGdiDdDDICreateProtectedSession_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", LPVOID),
                 ("reserve3", ULONG),
                 ("reserve4", LPVOID),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                ]
class NtGdiGetRegionData_arg3_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiGetRegionData_arg3_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiGetRegionData_arg3_struct2)
                )

class NtGdiGetRegionData_arg3_struct0(Structure):
     _fields_ = [("reserve0", NtGdiGetRegionData_arg3_struct1),
                 ("reserve1", BYTE*1)
                ]
class NtReadVirtualMemory_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIDestroyOverlay_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserCreateWindowEx_arg2_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT)
                ]

class NtUserCreateWindowEx_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", POINTER(NtUserCreateWindowEx_arg2_struct1)),
                 ("reserve1", ULONG)
                )
class NtUserCreateWindowEx_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT)
                ]

class NtUserCreateWindowEx_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", POINTER(NtUserCreateWindowEx_arg3_struct1)),
                 ("reserve1", ULONG)
                )
class NtUserCreateWindowEx_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", c_char_p)
                ]
class NtUserCreateWindowEx_arg17_struct0(Structure):
     _fields_ = [("reserve0", USHORT)
                ]
class NtUserFlashWindowEx_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG)
                ]
class NtGdiDdDDIDestroyProtectedSession_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIGetPostCompositionCaps_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtQueryMultipleValueKey_arg2_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtQueryMultipleValueKey_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", POINTER(NtQueryMultipleValueKey_arg2_struct1)),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                )
class NtGdiFONTOBJ_pifi_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiFONTOBJ_pifi_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", NtGdiFONTOBJ_pifi_arg1_struct1),
                 ("reserve7", ULONG),
                 ("reserve8", POINTER(ULONG)),
                 ("reserve9", POINTER(ULONG))
                ]
class NtGdiXLATEOBJ_iXlate_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiDdDDIEvict_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIEvict_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", NtGdiDdDDIEvict_arg1_struct1),
                 ("reserve4", ULONG)
                )
class NtDxgkSubmitPresentBltToHwQueue_arg1_struct6(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]

class NtDxgkSubmitPresentBltToHwQueue_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtDxgkSubmitPresentBltToHwQueue_arg1_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtDxgkSubmitPresentBltToHwQueue_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtDxgkSubmitPresentBltToHwQueue_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtDxgkSubmitPresentBltToHwQueue_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", NtDxgkSubmitPresentBltToHwQueue_arg1_struct2),
                 ("reserve7", NtDxgkSubmitPresentBltToHwQueue_arg1_struct3),
                 ("reserve8", ULONG),
                 ("reserve9", POINTER(NtDxgkSubmitPresentBltToHwQueue_arg1_struct4)),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", NtDxgkSubmitPresentBltToHwQueue_arg1_struct5),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG*64),
                 ("reserve15", ULONG),
                 ("reserve16", NtDxgkSubmitPresentBltToHwQueue_arg1_struct6)
                )

class NtDxgkSubmitPresentBltToHwQueue_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtDxgkSubmitPresentBltToHwQueue_arg1_struct1)
                )
class NtGdiDdDDICreateOutputDupl_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDICreateOutputDupl_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDICreateOutputDupl_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiDdDDICreateOutputDupl_arg1_struct1*3),
                 ("reserve5", NtGdiDdDDICreateOutputDupl_arg1_struct2)
                )
class NtCancelIoFileEx_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtCancelIoFileEx_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtCancelIoFileEx_arg2_struct1),
                 ("reserve3", ULONG)
                )
class NtCancelIoFileEx_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiEngStretchBlt_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngStretchBlt_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngStretchBlt_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngStretchBlt_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngStretchBlt_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngStretchBlt_arg2_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngStretchBlt_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngStretchBlt_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngStretchBlt_arg3_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngStretchBlt_arg4_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngStretchBlt_arg4_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiEngStretchBlt_arg4_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtGdiEngStretchBlt_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiEngStretchBlt_arg6_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", USHORT),
                 ("reserve6", USHORT),
                 ("reserve7", USHORT),
                 ("reserve8", USHORT),
                 ("reserve9", USHORT),
                 ("reserve10", USHORT),
                 ("reserve11", USHORT)
                ]
class NtGdiEngStretchBlt_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiEngStretchBlt_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiEngStretchBlt_arg9_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiEngStretchBlt_arg10_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtSetInformationFile_arg2_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtUserGetClipboardData_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtWriteVirtualMemory_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtWriteVirtualMemory_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiSetBoundsRect_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiDdDDICreateDevice_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDICreateDevice_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]

class NtGdiDdDDICreateDevice_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", POINTER(ULONG)),
                 ("reserve4", ULONG),
                 ("reserve5", POINTER(NtGdiDdDDICreateDevice_arg1_struct1)),
                 ("reserve6", ULONG),
                 ("reserve7", POINTER(NtGdiDdDDICreateDevice_arg1_struct2)),
                 ("reserve8", ULONG)
                )
class NtGdiGetKerningPairs_arg3_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", ULONG)
                ]
class NtCancelSynchronousIoFile_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtNotifyChangeDirectoryFileEx_arg5_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtNotifyChangeDirectoryFileEx_arg5_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtNotifyChangeDirectoryFileEx_arg5_struct1),
                 ("reserve3", ULONG)
                )
class NtQueryInformationAtom_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiModifyWorldTransform_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]
class NtUserDrawAnimatedRects_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUserDrawAnimatedRects_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUserGetRawInputBuffer_arg1_struct2(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]

class NtUserGetRawInputBuffer_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", POINTER(ULONG))
                ]

class NtUserGetRawInputBuffer_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtUserGetRawInputBuffer_arg1_struct1),
                 ("reserve1", NtUserGetRawInputBuffer_arg1_struct2)
                )
class NtGdiDdDDISignalSynchronizationObjectFromGpu_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", LPVOID),
                 ("reserve3", c_longlong*8)
                ]
class NtGdiDdDDIOpenResourceFromNtHandle_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG*6)
                ]

class NtGdiDdDDIOpenResourceFromNtHandle_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", LPVOID),
                 ("reserve4", ULONG),
                 ("reserve5", LPVOID),
                 ("reserve6", ULONG),
                 ("reserve7", LPVOID),
                 ("reserve8", ULONG),
                 ("reserve9", LPVOID),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", POINTER(ULONG)),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG)
                ]
class NtGdiDdDDIGetContextInProcessSchedulingPriority_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiDoPalette_arg4_struct0(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE)
                ]
class NtConnectPort_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtConnectPort_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT)
                ]
class NtConnectPort_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtConnectPort_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtConnectPort_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIOutputDuplPresent_arg1_struct6(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIOutputDuplPresent_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIOutputDuplPresent_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIOutputDuplPresent_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDIOutputDuplPresent_arg1_struct3(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiDdDDIOutputDuplPresent_arg1_struct4),
                 ("reserve1", NtGdiDdDDIOutputDuplPresent_arg1_struct5)
                )

class NtGdiDdDDIOutputDuplPresent_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", LPVOID),
                 ("reserve2", ULONG),
                 ("reserve3", LPVOID)
                )

class NtGdiDdDDIOutputDuplPresent_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG*64),
                 ("reserve5", NtGdiDdDDIOutputDuplPresent_arg1_struct1),
                 ("reserve6", NtGdiDdDDIOutputDuplPresent_arg1_struct6),
                 ("reserve7", ULONG)
                )
class NtUserSetGestureConfig_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtOpenPrivateNamespace_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiSetBitmapDimension_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserInjectDeviceInput_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", ULONG),
                 ("reserve3", USHORT)
                ]
class NtUserGetImeHotKey_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetImeHotKey_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetImeHotKey_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetDManipHookInitFunction_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetDManipHookInitFunction_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIRender_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDIRender_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]

class NtGdiDdDDIRender_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", POINTER(ULONG)),
                 ("reserve6", ULONG),
                 ("reserve7", POINTER(NtGdiDdDDIRender_arg1_struct1)),
                 ("reserve8", ULONG),
                 ("reserve9", POINTER(NtGdiDdDDIRender_arg1_struct2)),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG*64),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", POINTER(ULONG)),
                 ("reserve18", ULONG)
                ]
class NtGdiCreateDIBSection_arg4_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG)
                ]

class NtGdiCreateDIBSection_arg4_struct0(Structure):
     _fields_ = [("reserve0", NtGdiCreateDIBSection_arg4_struct1),
                 ("reserve1", ULONG*1)
                ]
class NtPrivilegeObjectAuditAlarm_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtPrivilegeObjectAuditAlarm_arg5_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtPrivilegeObjectAuditAlarm_arg5_struct1(ctypes.Structure):
     _fields_ = (("reserve0", NtPrivilegeObjectAuditAlarm_arg5_struct2),
                 ("reserve1", ULONG)
                )

class NtPrivilegeObjectAuditAlarm_arg5_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtPrivilegeObjectAuditAlarm_arg5_struct1*341)
                )
class NtQueryInformationFile_arg2_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtGdiCLIPOBJ_bEnum_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiCLIPOBJ_bEnum_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiCLIPOBJ_bEnum_arg1_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtRenameKey_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGdiCreateColorTransform_arg2_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]

class NtGdiCreateColorTransform_arg2_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]

class NtGdiCreateColorTransform_arg2_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]

class NtGdiCreateColorTransform_arg2_struct1(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiCreateColorTransform_arg2_struct2),
                 ("reserve1", NtGdiCreateColorTransform_arg2_struct3),
                 ("reserve2", NtGdiCreateColorTransform_arg2_struct4)
                )

class NtGdiCreateColorTransform_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", NtGdiCreateColorTransform_arg2_struct1),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", c_char*2048)
                )
class NtUserInjectGesture_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG)
                ]
class NtUserInjectKeyboardInput_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG)
                ]
class NtAccessCheck_arg1_struct1(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG*1024)
                ]

class NtAccessCheck_arg1_struct3(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheck_arg1_struct2(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheck_arg1_struct3),
                 ("reserve3", ULONG*1024)
                ]

class NtAccessCheck_arg1_struct4(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtAccessCheck_arg1_struct5(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtAccessCheck_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", BYTE),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtAccessCheck_arg1_struct1)),
                 ("reserve3", POINTER(NtAccessCheck_arg1_struct2)),
                 ("reserve4", POINTER(NtAccessCheck_arg1_struct4)),
                 ("reserve5", POINTER(NtAccessCheck_arg1_struct5))
                )
class NtAccessCheck_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtAccessCheck_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtAccessCheck_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtAccessCheck_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtAccessCheck_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIGetRuntimeData_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", ULONG)
                ]
class NtGdiEngBitBlt_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngBitBlt_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngBitBlt_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngBitBlt_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngBitBlt_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngBitBlt_arg2_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngBitBlt_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngBitBlt_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngBitBlt_arg3_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngBitBlt_arg4_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngBitBlt_arg4_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiEngBitBlt_arg4_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtGdiEngBitBlt_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiEngBitBlt_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiEngBitBlt_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiEngBitBlt_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiEngBitBlt_arg9_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtGdiEngBitBlt_arg10_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserHwndQueryRedirectionInfo_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserHwndQueryRedirectionInfo_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateTimer2_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", c_char_p),
                 ("reserve4", ULONG),
                 ("reserve5", USHORT),
                 ("reserve6", USHORT),
                 ("reserve7", c_longlong*2),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", USHORT),
                 ("reserve15", USHORT),
                 ("reserve16", c_longlong*2),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG)
                ]
class NtCreateTimer2_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]
class NtGdiDdDDIAcquireKeyedMutex2_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(c_longlong)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", ULONG)
                ]
class NtOpenResourceManager_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]
class NtOpenResourceManager_arg5_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenResourceManager_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenResourceManager_arg5_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtOpenKey_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenKey_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenKey_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiDdDDICheckVidPnExclusiveOwnership_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserDrawCaptionTemp_arg6_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserBuildHwndList_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserBuildHwndList_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUnlockFile_arg2_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDIDestroyAllocation2_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIDestroyAllocation2_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiDdDDIDestroyAllocation2_arg1_struct1)
                )
class NtUserGetClassInfoEx_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserGetClassInfoEx_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", c_char_p),
                 ("reserve10", c_char_p),
                 ("reserve11", ULONG)
                ]
class NtUserGetClassInfoEx_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", c_char*2048)
                ]
class NtGdiDdDDIReclaimAllocations_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", POINTER(ULONG)),
                 ("reserve4", ULONG)
                ]
class NtDeleteObjectAuditAlarm_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGdiGetDCPoint_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserOpenWindowStation_arg1_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtUserOpenWindowStation_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtUserOpenWindowStation_arg1_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                )
class NtResumeThread_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserGetGestureConfig_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtAccessCheckByType_arg1_struct2(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckByType_arg1_struct1(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckByType_arg1_struct2),
                 ("reserve3", ULONG*1024)
                ]

class NtAccessCheckByType_arg1_struct4(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckByType_arg1_struct3(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckByType_arg1_struct4),
                 ("reserve3", ULONG*1024)
                ]

class NtAccessCheckByType_arg1_struct5(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtAccessCheckByType_arg1_struct6(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtAccessCheckByType_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", POINTER(NtAccessCheckByType_arg1_struct1)),
                 ("reserve4", POINTER(NtAccessCheckByType_arg1_struct3)),
                 ("reserve5", POINTER(NtAccessCheckByType_arg1_struct5)),
                 ("reserve6", POINTER(NtAccessCheckByType_arg1_struct6))
                )
class NtAccessCheckByType_arg2_struct1(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckByType_arg2_struct0(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckByType_arg2_struct1),
                 ("reserve3", ULONG*1024)
                ]
class NtAccessCheckByType_arg5_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]

class NtAccessCheckByType_arg5_struct0(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtAccessCheckByType_arg5_struct1))
                )
class NtAccessCheckByType_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtAccessCheckByType_arg8_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtAccessCheckByType_arg8_struct1(ctypes.Structure):
     _fields_ = (("reserve0", NtAccessCheckByType_arg8_struct2),
                 ("reserve1", ULONG)
                )

class NtAccessCheckByType_arg8_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtAccessCheckByType_arg8_struct1*341)
                )
class NtAccessCheckByType_arg11_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIOpenNtHandleFromName_arg1_struct2(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtGdiDdDDIOpenNtHandleFromName_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtGdiDdDDIOpenNtHandleFromName_arg1_struct2)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]

class NtGdiDdDDIOpenNtHandleFromName_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", POINTER(NtGdiDdDDIOpenNtHandleFromName_arg1_struct1)),
                 ("reserve2", ULONG)
                )
class NtUserSetClipboardData_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserGetClassName_arg3_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGdiSTROBJ_vEnumStart_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiSTROBJ_vEnumStart_arg1_struct6(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiSTROBJ_vEnumStart_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiSTROBJ_vEnumStart_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiSTROBJ_vEnumStart_arg1_struct3(Structure):
     _fields_ = [("reserve0", NtGdiSTROBJ_vEnumStart_arg1_struct4),
                 ("reserve1", NtGdiSTROBJ_vEnumStart_arg1_struct5),
                 ("reserve2", BYTE*1)
                ]

class NtGdiSTROBJ_vEnumStart_arg1_struct2(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", LPVOID),
                 ("reserve2", NtGdiSTROBJ_vEnumStart_arg1_struct6)
                )

class NtGdiSTROBJ_vEnumStart_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiSTROBJ_vEnumStart_arg1_struct1),
                 ("reserve4", POINTER(NtGdiSTROBJ_vEnumStart_arg1_struct2)),
                 ("reserve5", c_char_p)
                ]
class NtGdiDdDDIDestroyHwQueue_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDISetVidPnSourceHwProtection_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtGdiDdDDIWaitForVerticalBlankEvent_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtGdiDdDDIGetScanLine_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", BYTE),
                 ("reserve3", ULONG)
                ]
class NtUserFindWindowEx_arg3_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserFindWindowEx_arg4_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserGetHimetricScaleFactorFromPixelLocation_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetHimetricScaleFactorFromPixelLocation_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateJobObject_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateDirectoryObjectEx_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateDirectoryObjectEx_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtCreateDirectoryObjectEx_arg3_struct4(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtCreateDirectoryObjectEx_arg3_struct3(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtCreateDirectoryObjectEx_arg3_struct4),
                 ("reserve3", ULONG*1024)
                ]

class NtCreateDirectoryObjectEx_arg3_struct6(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtCreateDirectoryObjectEx_arg3_struct5(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtCreateDirectoryObjectEx_arg3_struct6),
                 ("reserve3", ULONG*1024)
                ]

class NtCreateDirectoryObjectEx_arg3_struct7(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtCreateDirectoryObjectEx_arg3_struct8(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtCreateDirectoryObjectEx_arg3_struct2(ctypes.Structure):
     _fields_ = (("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", POINTER(NtCreateDirectoryObjectEx_arg3_struct3)),
                 ("reserve4", POINTER(NtCreateDirectoryObjectEx_arg3_struct5)),
                 ("reserve5", POINTER(NtCreateDirectoryObjectEx_arg3_struct7)),
                 ("reserve6", POINTER(NtCreateDirectoryObjectEx_arg3_struct8))
                )

class NtCreateDirectoryObjectEx_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateDirectoryObjectEx_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(NtCreateDirectoryObjectEx_arg3_struct2)),
                 ("reserve5", ULONG)
                )
class NtGdiDdDDIDestroyOutputDupl_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtAlpcConnectPort_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtAlpcConnectPort_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtAlpcConnectPort_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG)
                ]
class NtAlpcConnectPort_arg6_struct0(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", ULONG)
                ]
class NtAlpcConnectPort_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtAlpcConnectPort_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtAlpcConnectPort_arg11_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserDisplayConfigSetDeviceInfo_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserDisplayConfigSetDeviceInfo_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtUserDisplayConfigSetDeviceInfo_arg1_struct1),
                 ("reserve3", ULONG)
                )
class NtGdiDdDDIGetDWMVerticalBlankEvent_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", POINTER(ULONG))
                ]
class NtUserProcessConnect_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateWaitCompletionPacket_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", c_longlong*2),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT),
                 ("reserve13", c_longlong*2),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG)
                ]
class NtGdiDdDDISetAllocationPriority_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG))
                ]
class NtGdiCLIPOBJ_cEnumStart_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiCLIPOBJ_cEnumStart_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiCLIPOBJ_cEnumStart_arg1_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtUserDisplayConfigGetDeviceInfo_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtUserDisplayConfigGetDeviceInfo_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtUserDisplayConfigGetDeviceInfo_arg1_struct1),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG)
                )
class NtGdiGetOutlineTextMetricsInternalW_arg3_struct7(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiGetOutlineTextMetricsInternalW_arg3_struct6(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiGetOutlineTextMetricsInternalW_arg3_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiGetOutlineTextMetricsInternalW_arg3_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiGetOutlineTextMetricsInternalW_arg3_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiGetOutlineTextMetricsInternalW_arg3_struct2(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE),
                 ("reserve6", BYTE),
                 ("reserve7", BYTE),
                 ("reserve8", BYTE),
                 ("reserve9", BYTE)
                ]

class NtGdiGetOutlineTextMetricsInternalW_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT),
                 ("reserve13", USHORT),
                 ("reserve14", USHORT),
                 ("reserve15", BYTE),
                 ("reserve16", BYTE),
                 ("reserve17", BYTE),
                 ("reserve18", BYTE),
                 ("reserve19", BYTE)
                ]

class NtGdiGetOutlineTextMetricsInternalW_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", NtGdiGetOutlineTextMetricsInternalW_arg3_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", NtGdiGetOutlineTextMetricsInternalW_arg3_struct2),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", NtGdiGetOutlineTextMetricsInternalW_arg3_struct3),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", NtGdiGetOutlineTextMetricsInternalW_arg3_struct4),
                 ("reserve21", NtGdiGetOutlineTextMetricsInternalW_arg3_struct5),
                 ("reserve22", NtGdiGetOutlineTextMetricsInternalW_arg3_struct6),
                 ("reserve23", NtGdiGetOutlineTextMetricsInternalW_arg3_struct7),
                 ("reserve24", ULONG),
                 ("reserve25", ULONG),
                 ("reserve26", ULONG),
                 ("reserve27", ULONG),
                 ("reserve28", c_char_p),
                 ("reserve29", c_char_p),
                 ("reserve30", c_char_p),
                 ("reserve31", c_char_p)
                ]
class NtOpenThread_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtOpenThread_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiCreateDIBitmapInternal_arg6_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG)
                ]

class NtGdiCreateDIBitmapInternal_arg6_struct0(Structure):
     _fields_ = [("reserve0", NtGdiCreateDIBitmapInternal_arg6_struct1),
                 ("reserve1", ULONG*1)
                ]
class NtReleaseSemaphore_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIOpenKeyedMutex2_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", ULONG)
                ]
class NtCancelWaitCompletionPacket_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG)
                ]
class NtGdiGetETM_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", USHORT),
                 ("reserve6", USHORT),
                 ("reserve7", USHORT),
                 ("reserve8", USHORT),
                 ("reserve9", USHORT),
                 ("reserve10", USHORT),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT),
                 ("reserve13", USHORT),
                 ("reserve14", USHORT),
                 ("reserve15", USHORT),
                 ("reserve16", USHORT),
                 ("reserve17", USHORT),
                 ("reserve18", USHORT),
                 ("reserve19", USHORT),
                 ("reserve20", USHORT),
                 ("reserve21", USHORT),
                 ("reserve22", USHORT),
                 ("reserve23", USHORT),
                 ("reserve24", USHORT),
                 ("reserve25", USHORT)
                ]
class NtGdiDdDDISetDisplayMode_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", BYTE)
                ]
class NtSignalAndWaitForSingleObject_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDIInvalidateActiveVidPn_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtUserGetProcessUIContextInformation_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDISetHwProtectionTeardownRecovery_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiGetTextCharsetInfo_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG*4),
                 ("reserve1", ULONG*2)
                ]
class NtRIMGetDevicePropertiesLockfree_arg2_struct4(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT)
                ]

class NtRIMGetDevicePropertiesLockfree_arg2_struct3(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT)
                ]

class NtRIMGetDevicePropertiesLockfree_arg2_struct2(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE)
                ]

class NtRIMGetDevicePropertiesLockfree_arg2_struct1(ctypes.Structure):
     _fields_ = (("reserve0", NtRIMGetDevicePropertiesLockfree_arg2_struct2),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", ULONG),
                 ("reserve6", NtRIMGetDevicePropertiesLockfree_arg2_struct3),
                 ("reserve7", NtRIMGetDevicePropertiesLockfree_arg2_struct4)
                )

class NtRIMGetDevicePropertiesLockfree_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtRIMGetDevicePropertiesLockfree_arg2_struct1)
                )
class NtUserOpenClipboard_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtOpenJobObject_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtOpenJobObject_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenJobObject_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenJobObject_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", USHORT),
                 ("reserve7", USHORT),
                 ("reserve8", c_char_p)
                ]
class NtGdiPolyPolyDraw_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiPolyDraw_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserCreateDesktopEx_arg1_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtUserCreateDesktopEx_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtUserCreateDesktopEx_arg1_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", ULONG)
                ]
class NtUserCreateDesktopEx_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserCreateDesktopEx_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT)
                ]

class NtUserCreateDesktopEx_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", c_char*72),
                 ("reserve1", ULONG),
                 ("reserve2", NtUserCreateDesktopEx_arg3_struct1),
                 ("reserve3", c_char*2048)
                )
class NtUserBeginPaint_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIAdjustFullscreenGamma_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]

class NtGdiDdDDIAdjustFullscreenGamma_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]

class NtGdiDdDDIAdjustFullscreenGamma_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiDdDDIAdjustFullscreenGamma_arg1_struct1),
                 ("reserve3", NtGdiDdDDIAdjustFullscreenGamma_arg1_struct2)
                )
class NtUserInvalidateRect_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiDdDDISubmitCommand_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG*64),
                 ("reserve6", POINTER(ULONG)),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG*16),
                 ("reserve10", ULONG),
                 ("reserve11", POINTER(ULONG))
                ]
class NtGdiDdDDIGetOverlayState_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", BYTE)
                ]
class NtGdiDdDDIOpenAdapterFromDeviceName_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDIOpenAdapterFromDeviceName_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", c_char_p),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiDdDDIOpenAdapterFromDeviceName_arg1_struct1)
                )
class NtGdiDdDDIReleaseKeyedMutex2_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", POINTER(ULONG)),
                 ("reserve4", ULONG)
                ]
class NtUserGetPointerDevices_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", USHORT),
                 ("reserve6", c_char*2048)
                ]
class NtGdiDdDDIQueryAllocationResidency_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG))
                ]
class NtUserGetPointerDeviceProperties_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", USHORT),
                 ("reserve7", USHORT)
                ]
class NtGdiFONTOBJ_cGetAllGlyphHandles_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiFONTOBJ_cGetAllGlyphHandles_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", NtGdiFONTOBJ_cGetAllGlyphHandles_arg1_struct1),
                 ("reserve7", ULONG),
                 ("reserve8", POINTER(ULONG)),
                 ("reserve9", POINTER(ULONG))
                ]
class NtGdiDdDDISetContextInProcessSchedulingPriority_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserLockCursor_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtCreateMailslotFile_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateMailslotFile_arg3_struct2(Structure):
     _fields_ = [("reserve0", c_char*2048)
                ]

class NtCreateMailslotFile_arg3_struct1(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtCreateMailslotFile_arg3_struct2))
                )

class NtCreateMailslotFile_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateMailslotFile_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", ULONG)
                ]
class NtCreateMailslotFile_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateMailslotFile_arg8_struct1(Structure):
     _fields_ = [("reserve0", c_char*2048)
                ]

class NtCreateMailslotFile_arg8_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateMailslotFile_arg8_struct1))
                )
class NtAllocateLocallyUniqueId_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserGetPointerDeviceRects_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUserGetPointerDeviceRects_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUserTrackPopupMenuEx_arg6_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtUserTrackPopupMenuEx_arg6_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtUserTrackPopupMenuEx_arg6_struct1)
                )
class NtUserTranslateAccelerator_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserTranslateAccelerator_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", POINTER(ULONG)),
                 ("reserve4", ULONG),
                 ("reserve5", NtUserTranslateAccelerator_arg3_struct1),
                 ("reserve6", ULONG)
                )
class NtGdiGetColorAdjustment_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", USHORT),
                 ("reserve6", USHORT),
                 ("reserve7", USHORT),
                 ("reserve8", USHORT),
                 ("reserve9", USHORT),
                 ("reserve10", USHORT),
                 ("reserve11", USHORT)
                ]
class NtUserGetCursorDims_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtSetSystemTime_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtFlushBuffersFile_arg2_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtUserGetMenuItemRect_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUserThunkedMenuInfo_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                ]
class NtGdiDdDDIOpenSynchronizationObject_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", c_longlong*8)
                ]
class NtGdiDdDDIQueryProtectedSessionInfoFromNtHandle_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", LPVOID),
                 ("reserve2", ULONG),
                 ("reserve3", LPVOID),
                 ("reserve4", ULONG)
                ]
class NtQueryPerformanceCounter_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtQueryPerformanceCounter_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIGetProcessDeviceRemovalSupport_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDIGetProcessDeviceRemovalSupport_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDIGetProcessDeviceRemovalSupport_arg1_struct1),
                 ("reserve2", BYTE)
                )
class NtAdjustGroupsToken_arg3_struct3(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAdjustGroupsToken_arg3_struct2(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAdjustGroupsToken_arg3_struct3),
                 ("reserve3", ULONG*1024)
                ]

class NtAdjustGroupsToken_arg3_struct1(ctypes.Structure):
     _fields_ = (("reserve0", POINTER(NtAdjustGroupsToken_arg3_struct2)),
                 ("reserve1", ULONG)
                )

class NtAdjustGroupsToken_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtAdjustGroupsToken_arg3_struct1*512)
                )
class NtAdjustGroupsToken_arg5_struct3(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAdjustGroupsToken_arg5_struct2(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAdjustGroupsToken_arg5_struct3),
                 ("reserve3", ULONG*1024)
                ]

class NtAdjustGroupsToken_arg5_struct1(ctypes.Structure):
     _fields_ = (("reserve0", POINTER(NtAdjustGroupsToken_arg5_struct2)),
                 ("reserve1", ULONG)
                )

class NtAdjustGroupsToken_arg5_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtAdjustGroupsToken_arg5_struct1*512)
                )
class NtInitializeNlsFiles_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtInitializeNlsFiles_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtInitializeNlsFiles_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIQueryResourceInfoFromNtHandle_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                ]
class NtGdiDdDDIOfferAllocations_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIOfferAllocations_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", NtGdiDdDDIOfferAllocations_arg1_struct1)
                )
class NtGetNlsSectionPtr_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGetNlsSectionPtr_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtFindAtom_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtFindAtom_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", BYTE),
                 ("reserve2", BYTE),
                 ("reserve3", POINTER(NtFindAtom_arg3_struct1))
                )
class NtUserSetScrollInfo_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                ]
class NtSetInformationDebugObject_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiGetPerBandInfo_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiGetPerBandInfo_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiGetPerBandInfo_arg2_struct1),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                )
class NtAccessCheckAndAuditAlarm_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtAccessCheckAndAuditAlarm_arg3_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtAccessCheckAndAuditAlarm_arg4_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtAccessCheckAndAuditAlarm_arg5_struct2(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckAndAuditAlarm_arg5_struct1(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckAndAuditAlarm_arg5_struct2),
                 ("reserve3", ULONG*1024)
                ]

class NtAccessCheckAndAuditAlarm_arg5_struct4(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckAndAuditAlarm_arg5_struct3(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckAndAuditAlarm_arg5_struct4),
                 ("reserve3", ULONG*1024)
                ]

class NtAccessCheckAndAuditAlarm_arg5_struct5(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtAccessCheckAndAuditAlarm_arg5_struct6(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtAccessCheckAndAuditAlarm_arg5_struct0(ctypes.Structure):
     _fields_ = (("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", POINTER(NtAccessCheckAndAuditAlarm_arg5_struct1)),
                 ("reserve4", POINTER(NtAccessCheckAndAuditAlarm_arg5_struct3)),
                 ("reserve5", POINTER(NtAccessCheckAndAuditAlarm_arg5_struct5)),
                 ("reserve6", POINTER(NtAccessCheckAndAuditAlarm_arg5_struct6))
                )
class NtAccessCheckAndAuditAlarm_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiDdDDIFlipOverlay_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", POINTER(ULONG)),
                 ("reserve4", ULONG)
                ]
class NtUserMNDragOver_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserMNDragOver_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUserHwndSetRedirectionInfo_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetTouchInputInfo_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetWOWClass_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT)
                ]
class NtGdiSetDIBitsToDeviceInternal_arg11_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG)
                ]

class NtGdiSetDIBitsToDeviceInternal_arg11_struct0(Structure):
     _fields_ = [("reserve0", NtGdiSetDIBitsToDeviceInternal_arg11_struct1),
                 ("reserve1", ULONG*1)
                ]
class NtGdiDdDDISignalSynchronizationObjectFromGpu2_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDISignalSynchronizationObjectFromGpu2_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", LPVOID),
                 ("reserve2", NtGdiDdDDISignalSynchronizationObjectFromGpu2_arg1_struct1),
                 ("reserve3", ULONG),
                 ("reserve4", LPVOID),
                 ("reserve5", c_longlong*8)
                ]
class NtNotifyChangeMultipleKeys_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtNotifyChangeMultipleKeys_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtNotifyChangeMultipleKeys_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtNotifyChangeMultipleKeys_arg7_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtQueryFullAttributesFile_arg1_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtQueryFullAttributesFile_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtQueryFullAttributesFile_arg1_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtQueryFullAttributesFile_arg2_struct0(Structure):
     _fields_ = [("reserve0", c_longlong),
                 ("reserve1", c_longlong),
                 ("reserve2", c_longlong),
                 ("reserve3", c_longlong),
                 ("reserve4", c_longlong),
                 ("reserve5", c_longlong),
                 ("reserve6", ULONG)
                ]
class NtOpenEvent_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenEvent_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenEvent_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtQueryWnfStateData_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtQueryWnfStateData_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtQueryWnfStateData_arg5_struct0(Structure):
     _fields_ = [("reserve0", c_longlong*2)
                ]
class NtQueryWnfStateData_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserSetWindowPlacement_arg2_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtUserSetWindowPlacement_arg2_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtUserSetWindowPlacement_arg2_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserSetWindowPlacement_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserSetWindowPlacement_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtUserSetWindowPlacement_arg2_struct1),
                 ("reserve4", NtUserSetWindowPlacement_arg2_struct2),
                 ("reserve5", NtUserSetWindowPlacement_arg2_struct3),
                 ("reserve6", NtUserSetWindowPlacement_arg2_struct4)
                )
class NtUserCopyAcceleratorTable_arg2_struct0(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT)
                ]
class NtGdiDdDDIOpenKeyedMutexFromNtHandle_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", ULONG)
                ]
class NtUserCheckAccessForIntegrityLevel_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateRegistryTransaction_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtCreateRegistryTransaction_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateRegistryTransaction_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtUserScrollDC_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUserScrollDC_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUserScrollDC_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtSetIoCompletion_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtSetIoCompletion_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtSetIoCompletion_arg3_struct1),
                 ("reserve3", ULONG)
                )
class NtCreateThreadEx_arg1_struct0(Structure):
     _fields_ = [("reserve0", LPVOID)
                ]
class NtCreateThreadEx_arg11_struct2(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtCreateThreadEx_arg11_struct3(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", USHORT)
                ]

class NtCreateThreadEx_arg11_struct4(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG)
                ]

class NtCreateThreadEx_arg11_struct5(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT)
                ]

class NtCreateThreadEx_arg11_struct6(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", ULONG)
                ]

class NtCreateThreadEx_arg11_struct1(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", ULONG),
                 ("reserve3", POINTER(NtCreateThreadEx_arg11_struct2)),
                 ("reserve4", POINTER(NtCreateThreadEx_arg11_struct3)),
                 ("reserve5", POINTER(NtCreateThreadEx_arg11_struct4)),
                 ("reserve6", POINTER(NtCreateThreadEx_arg11_struct5)),
                 ("reserve7", POINTER(NtCreateThreadEx_arg11_struct6)),
                 ("reserve8", ULONG)
                )

class NtCreateThreadEx_arg11_struct7(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtCreateThreadEx_arg11_struct8(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", USHORT)
                ]

class NtCreateThreadEx_arg11_struct9(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG)
                ]

class NtCreateThreadEx_arg11_struct10(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT)
                ]

class NtCreateThreadEx_arg11_struct11(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", ULONG)
                ]

class NtCreateThreadEx_arg11_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", POINTER(NtCreateThreadEx_arg11_struct1)),
                 ("reserve4", USHORT),
                 ("reserve5", USHORT),
                 ("reserve6", USHORT),
                 ("reserve7", USHORT),
                 ("reserve8", ULONG),
                 ("reserve9", POINTER(NtCreateThreadEx_arg11_struct7)),
                 ("reserve10", POINTER(NtCreateThreadEx_arg11_struct8)),
                 ("reserve11", POINTER(NtCreateThreadEx_arg11_struct9)),
                 ("reserve12", POINTER(NtCreateThreadEx_arg11_struct10)),
                 ("reserve13", POINTER(NtCreateThreadEx_arg11_struct11)),
                 ("reserve14", ULONG)
                )
class NtGdiBRUSHOBJ_hGetColorTransform_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtGdiPlgBlt_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiFONTOBJ_pxoGetXform_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiFONTOBJ_pxoGetXform_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", NtGdiFONTOBJ_pxoGetXform_arg1_struct1),
                 ("reserve7", ULONG),
                 ("reserve8", POINTER(ULONG)),
                 ("reserve9", POINTER(ULONG))
                ]
class NtGdiEngCopyBits_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngCopyBits_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngCopyBits_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngCopyBits_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngCopyBits_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngCopyBits_arg2_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngCopyBits_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngCopyBits_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiEngCopyBits_arg3_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtGdiEngCopyBits_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiEngCopyBits_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiEngCopyBits_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserGetHDevName_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateNamedPipeFile_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateNamedPipeFile_arg3_struct2(Structure):
     _fields_ = [("reserve0", c_char*2048)
                ]

class NtCreateNamedPipeFile_arg3_struct1(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtCreateNamedPipeFile_arg3_struct2))
                )

class NtCreateNamedPipeFile_arg3_struct5(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtCreateNamedPipeFile_arg3_struct4(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtCreateNamedPipeFile_arg3_struct5),
                 ("reserve3", ULONG*1024)
                ]

class NtCreateNamedPipeFile_arg3_struct7(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtCreateNamedPipeFile_arg3_struct6(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtCreateNamedPipeFile_arg3_struct7),
                 ("reserve3", ULONG*1024)
                ]

class NtCreateNamedPipeFile_arg3_struct8(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtCreateNamedPipeFile_arg3_struct9(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtCreateNamedPipeFile_arg3_struct3(ctypes.Structure):
     _fields_ = (("reserve0", BYTE),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtCreateNamedPipeFile_arg3_struct4)),
                 ("reserve3", POINTER(NtCreateNamedPipeFile_arg3_struct6)),
                 ("reserve4", POINTER(NtCreateNamedPipeFile_arg3_struct8)),
                 ("reserve5", POINTER(NtCreateNamedPipeFile_arg3_struct9))
                )

class NtCreateNamedPipeFile_arg3_struct11(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtCreateNamedPipeFile_arg3_struct10(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtCreateNamedPipeFile_arg3_struct11),
                 ("reserve3", ULONG*1024)
                ]

class NtCreateNamedPipeFile_arg3_struct13(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtCreateNamedPipeFile_arg3_struct12(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtCreateNamedPipeFile_arg3_struct13),
                 ("reserve3", ULONG*1024)
                ]

class NtCreateNamedPipeFile_arg3_struct14(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtCreateNamedPipeFile_arg3_struct15(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtCreateNamedPipeFile_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateNamedPipeFile_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(NtCreateNamedPipeFile_arg3_struct3)),
                 ("reserve5", ULONG),
                 ("reserve6", BYTE),
                 ("reserve7", USHORT),
                 ("reserve8", POINTER(NtCreateNamedPipeFile_arg3_struct10)),
                 ("reserve9", POINTER(NtCreateNamedPipeFile_arg3_struct12)),
                 ("reserve10", POINTER(NtCreateNamedPipeFile_arg3_struct14)),
                 ("reserve11", POINTER(NtCreateNamedPipeFile_arg3_struct15))
                )
class NtCreateNamedPipeFile_arg4_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtCreateNamedPipeFile_arg14_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG)
                ]
class NtQueryInformationJobObject_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiEngStretchBltROP_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngStretchBltROP_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngStretchBltROP_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngStretchBltROP_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngStretchBltROP_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngStretchBltROP_arg2_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngStretchBltROP_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngStretchBltROP_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngStretchBltROP_arg3_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngStretchBltROP_arg4_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngStretchBltROP_arg4_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiEngStretchBltROP_arg4_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtGdiEngStretchBltROP_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiEngStretchBltROP_arg6_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", USHORT),
                 ("reserve6", USHORT),
                 ("reserve7", USHORT),
                 ("reserve8", USHORT),
                 ("reserve9", USHORT),
                 ("reserve10", USHORT),
                 ("reserve11", USHORT)
                ]
class NtGdiEngStretchBltROP_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiEngStretchBltROP_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiEngStretchBltROP_arg9_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiEngStretchBltROP_arg10_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiEngStretchBltROP_arg12_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtGdiColorCorrectPalette_arg5_struct0(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE)
                ]
class NtGdiExtCreateRegion_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]
class NtGdiExtCreateRegion_arg3_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiExtCreateRegion_arg3_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiExtCreateRegion_arg3_struct2)
                )

class NtGdiExtCreateRegion_arg3_struct0(Structure):
     _fields_ = [("reserve0", NtGdiExtCreateRegion_arg3_struct1),
                 ("reserve1", BYTE*1)
                ]
class NtUserConvertMemHandle_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG)
                ]
class NtUserCreateLocalMemHandle_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIMarkDeviceAsError_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserGetCurrentInputMessageSource_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserGetGestureInfo_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiXLATEOBJ_cGetPalette_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiGradientFill_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", USHORT)
                ]
class NtUserGetClipboardFormatName_arg2_struct0(Structure):
     _fields_ = [("reserve0", c_char*2048)
                ]
class NtUserSetWindowsHookEx_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtUserBuildNameList_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetClipCursor_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUserMessageCall_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtAccessCheckByTypeResultListAndAuditAlarm_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtAccessCheckByTypeResultListAndAuditAlarm_arg3_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtAccessCheckByTypeResultListAndAuditAlarm_arg4_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtAccessCheckByTypeResultListAndAuditAlarm_arg5_struct2(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarm_arg5_struct1(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckByTypeResultListAndAuditAlarm_arg5_struct2),
                 ("reserve3", ULONG*1024)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarm_arg5_struct4(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarm_arg5_struct3(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckByTypeResultListAndAuditAlarm_arg5_struct4),
                 ("reserve3", ULONG*1024)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarm_arg5_struct5(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarm_arg5_struct6(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarm_arg5_struct0(ctypes.Structure):
     _fields_ = (("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", POINTER(NtAccessCheckByTypeResultListAndAuditAlarm_arg5_struct1)),
                 ("reserve4", POINTER(NtAccessCheckByTypeResultListAndAuditAlarm_arg5_struct3)),
                 ("reserve5", POINTER(NtAccessCheckByTypeResultListAndAuditAlarm_arg5_struct5)),
                 ("reserve6", POINTER(NtAccessCheckByTypeResultListAndAuditAlarm_arg5_struct6))
                )
class NtAccessCheckByTypeResultListAndAuditAlarm_arg6_struct1(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarm_arg6_struct0(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckByTypeResultListAndAuditAlarm_arg6_struct1),
                 ("reserve3", ULONG*1024)
                ]
class NtAccessCheckByTypeResultListAndAuditAlarm_arg10_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]

class NtAccessCheckByTypeResultListAndAuditAlarm_arg10_struct0(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtAccessCheckByTypeResultListAndAuditAlarm_arg10_struct1))
                )
class NtAccessCheckByTypeResultListAndAuditAlarm_arg12_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtCreateTransaction_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtCreateTransaction_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateTransaction_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtCreateTransaction_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]
class NtCreateTransaction_arg10_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGetCachedSigningLevel_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtLoadKeyEx_arg1_struct2(Structure):
     _fields_ = [("reserve0", c_char*2048)
                ]

class NtLoadKeyEx_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtLoadKeyEx_arg1_struct2))
                )

class NtLoadKeyEx_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtLoadKeyEx_arg1_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                )
class NtLoadKeyEx_arg2_struct2(Structure):
     _fields_ = [("reserve0", c_char*2048)
                ]

class NtLoadKeyEx_arg2_struct1(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtLoadKeyEx_arg2_struct2))
                )

class NtLoadKeyEx_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtLoadKeyEx_arg2_struct1)),
                 ("reserve3", ULONG)
                )
class NtLoadKeyEx_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiAddFontResourceW_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG*16)
                ]
class NtFsControlFile_arg5_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtGdiHT_Get8BPPFormatPalette_arg1_struct0(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE)
                ]
class NtPrivilegeCheck_arg2_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtPrivilegeCheck_arg2_struct1(ctypes.Structure):
     _fields_ = (("reserve0", NtPrivilegeCheck_arg2_struct2),
                 ("reserve1", ULONG)
                )

class NtPrivilegeCheck_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtPrivilegeCheck_arg2_struct1*341)
                )
class NtUserPhysicalToLogicalPoint_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtCancelIoFile_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtCreateCompositionInputSink_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateCompositionInputSink_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiEngPlgBlt_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngPlgBlt_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngPlgBlt_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngPlgBlt_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngPlgBlt_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngPlgBlt_arg2_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngPlgBlt_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngPlgBlt_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngPlgBlt_arg3_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngPlgBlt_arg4_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngPlgBlt_arg4_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiEngPlgBlt_arg4_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtGdiEngPlgBlt_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiEngPlgBlt_arg6_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", USHORT),
                 ("reserve6", USHORT),
                 ("reserve7", USHORT),
                 ("reserve8", USHORT),
                 ("reserve9", USHORT),
                 ("reserve10", USHORT),
                 ("reserve11", USHORT)
                ]
class NtGdiEngPlgBlt_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiEngPlgBlt_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiEngPlgBlt_arg9_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiEngPlgBlt_arg10_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserLogicalToPerMonitorDPIPhysicalPoint_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtConvertBetweenAuxiliaryCounterAndPerformanceCounter_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserInitializeGenericHidInjection_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]

class NtUserInitializeGenericHidInjection_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", NtUserInitializeGenericHidInjection_arg1_struct1),
                 ("reserve4", ULONG),
                 ("reserve5", c_char_p),
                 ("reserve6", USHORT),
                 ("reserve7", c_char_p),
                 ("reserve8", USHORT)
                ]
class NtGdiDdDDIWaitForSynchronizationObjectFromGpu_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", LPVOID),
                 ("reserve3", c_longlong*8)
                ]
class NtGdiEngStrokeAndFillPath_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngStrokeAndFillPath_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngStrokeAndFillPath_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngStrokeAndFillPath_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiEngStrokeAndFillPath_arg3_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngStrokeAndFillPath_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiEngStrokeAndFillPath_arg3_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtGdiEngStrokeAndFillPath_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiEngStrokeAndFillPath_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtGdiEngStrokeAndFillPath_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", POINTER(ULONG)),
                 ("reserve7", ULONG)
                ]
class NtGdiEngStrokeAndFillPath_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtGdiEngStrokeAndFillPath_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtReadFile_arg5_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtGdiAddFontMemResourceEx_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG*16)
                ]
class NtOpenMutant_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtOpenMutant_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenMutant_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenMutant_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", USHORT),
                 ("reserve7", USHORT),
                 ("reserve8", c_char_p)
                ]
class NtDisplayString_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtCreateKey_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtCreateKey_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateKey_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtCreateKey_arg5_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtAlpcSendWaitReceivePort_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG),
                 ("reserve23", ULONG),
                 ("reserve24", ULONG),
                 ("reserve25", ULONG),
                 ("reserve26", ULONG),
                 ("reserve27", ULONG),
                 ("reserve28", ULONG),
                 ("reserve29", ULONG),
                 ("reserve30", ULONG),
                 ("reserve31", ULONG),
                 ("reserve32", ULONG),
                 ("reserve33", ULONG),
                 ("reserve34", ULONG),
                 ("reserve35", ULONG),
                 ("reserve36", ULONG),
                 ("reserve37", ULONG),
                 ("reserve38", ULONG),
                 ("reserve39", ULONG),
                 ("reserve40", ULONG),
                 ("reserve41", ULONG),
                 ("reserve42", ULONG),
                 ("reserve43", ULONG),
                 ("reserve44", ULONG),
                 ("reserve45", ULONG),
                 ("reserve46", ULONG),
                 ("reserve47", ULONG),
                 ("reserve48", ULONG),
                 ("reserve49", ULONG),
                 ("reserve50", ULONG),
                 ("reserve51", ULONG),
                 ("reserve52", ULONG),
                 ("reserve53", ULONG),
                 ("reserve54", ULONG),
                 ("reserve55", ULONG),
                 ("reserve56", ULONG),
                 ("reserve57", ULONG),
                 ("reserve58", ULONG),
                 ("reserve59", ULONG),
                 ("reserve60", ULONG),
                 ("reserve61", ULONG),
                 ("reserve62", ULONG),
                 ("reserve63", ULONG),
                 ("reserve64", ULONG),
                 ("reserve65", ULONG),
                 ("reserve66", ULONG),
                 ("reserve67", ULONG),
                 ("reserve68", ULONG),
                 ("reserve69", ULONG),
                 ("reserve70", ULONG),
                 ("reserve71", ULONG),
                 ("reserve72", ULONG),
                 ("reserve73", ULONG),
                 ("reserve74", ULONG),
                 ("reserve75", ULONG),
                 ("reserve76", ULONG),
                 ("reserve77", ULONG),
                 ("reserve78", ULONG),
                 ("reserve79", ULONG),
                 ("reserve80", ULONG),
                 ("reserve81", ULONG),
                 ("reserve82", ULONG),
                 ("reserve83", ULONG),
                 ("reserve84", ULONG),
                 ("reserve85", ULONG),
                 ("reserve86", ULONG),
                 ("reserve87", ULONG),
                 ("reserve88", ULONG),
                 ("reserve89", ULONG),
                 ("reserve90", ULONG),
                 ("reserve91", ULONG),
                 ("reserve92", ULONG),
                 ("reserve93", ULONG),
                 ("reserve94", ULONG),
                 ("reserve95", ULONG),
                 ("reserve96", ULONG),
                 ("reserve97", ULONG),
                 ("reserve98", ULONG),
                 ("reserve99", ULONG),
                 ("reserve100", ULONG),
                 ("reserve101", ULONG),
                 ("reserve102", ULONG),
                 ("reserve103", ULONG),
                 ("reserve104", ULONG),
                 ("reserve105", ULONG),
                 ("reserve106", ULONG),
                 ("reserve107", ULONG),
                 ("reserve108", ULONG),
                 ("reserve109", ULONG),
                 ("reserve110", ULONG),
                 ("reserve111", ULONG),
                 ("reserve112", ULONG),
                 ("reserve113", ULONG),
                 ("reserve114", ULONG),
                 ("reserve115", ULONG),
                 ("reserve116", ULONG),
                 ("reserve117", ULONG),
                 ("reserve118", ULONG),
                 ("reserve119", ULONG),
                 ("reserve120", ULONG),
                 ("reserve121", ULONG),
                 ("reserve122", ULONG),
                 ("reserve123", ULONG),
                 ("reserve124", ULONG),
                 ("reserve125", ULONG),
                 ("reserve126", ULONG),
                 ("reserve127", ULONG),
                 ("reserve128", ULONG),
                 ("reserve129", ULONG),
                 ("reserve130", ULONG),
                 ("reserve131", ULONG),
                 ("reserve132", ULONG),
                 ("reserve133", ULONG),
                 ("reserve134", ULONG),
                 ("reserve135", ULONG),
                 ("reserve136", ULONG),
                 ("reserve137", ULONG),
                 ("reserve138", ULONG),
                 ("reserve139", ULONG),
                 ("reserve140", ULONG),
                 ("reserve141", ULONG),
                 ("reserve142", ULONG),
                 ("reserve143", ULONG),
                 ("reserve144", ULONG),
                 ("reserve145", ULONG),
                 ("reserve146", ULONG),
                 ("reserve147", ULONG),
                 ("reserve148", ULONG),
                 ("reserve149", ULONG),
                 ("reserve150", ULONG),
                 ("reserve151", ULONG),
                 ("reserve152", ULONG),
                 ("reserve153", ULONG),
                 ("reserve154", ULONG),
                 ("reserve155", ULONG),
                 ("reserve156", ULONG),
                 ("reserve157", ULONG),
                 ("reserve158", ULONG),
                 ("reserve159", ULONG),
                 ("reserve160", ULONG),
                 ("reserve161", ULONG),
                 ("reserve162", ULONG),
                 ("reserve163", ULONG),
                 ("reserve164", ULONG),
                 ("reserve165", ULONG),
                 ("reserve166", ULONG),
                 ("reserve167", ULONG),
                 ("reserve168", ULONG),
                 ("reserve169", ULONG),
                 ("reserve170", ULONG),
                 ("reserve171", ULONG),
                 ("reserve172", ULONG),
                 ("reserve173", ULONG),
                 ("reserve174", ULONG),
                 ("reserve175", ULONG),
                 ("reserve176", ULONG),
                 ("reserve177", ULONG),
                 ("reserve178", ULONG),
                 ("reserve179", ULONG),
                 ("reserve180", ULONG),
                 ("reserve181", ULONG),
                 ("reserve182", ULONG),
                 ("reserve183", ULONG),
                 ("reserve184", ULONG),
                 ("reserve185", ULONG),
                 ("reserve186", ULONG),
                 ("reserve187", ULONG),
                 ("reserve188", ULONG),
                 ("reserve189", ULONG),
                 ("reserve190", ULONG),
                 ("reserve191", ULONG),
                 ("reserve192", ULONG),
                 ("reserve193", ULONG),
                 ("reserve194", ULONG),
                 ("reserve195", ULONG),
                 ("reserve196", ULONG),
                 ("reserve197", ULONG),
                 ("reserve198", ULONG),
                 ("reserve199", ULONG),
                 ("reserve200", ULONG),
                 ("reserve201", ULONG),
                 ("reserve202", ULONG),
                 ("reserve203", ULONG),
                 ("reserve204", ULONG),
                 ("reserve205", ULONG),
                 ("reserve206", ULONG),
                 ("reserve207", ULONG),
                 ("reserve208", ULONG),
                 ("reserve209", ULONG),
                 ("reserve210", ULONG),
                 ("reserve211", ULONG),
                 ("reserve212", ULONG),
                 ("reserve213", ULONG),
                 ("reserve214", ULONG),
                 ("reserve215", ULONG),
                 ("reserve216", ULONG),
                 ("reserve217", ULONG),
                 ("reserve218", ULONG),
                 ("reserve219", ULONG),
                 ("reserve220", ULONG),
                 ("reserve221", ULONG),
                 ("reserve222", ULONG),
                 ("reserve223", ULONG),
                 ("reserve224", ULONG),
                 ("reserve225", ULONG),
                 ("reserve226", ULONG),
                 ("reserve227", ULONG),
                 ("reserve228", ULONG),
                 ("reserve229", ULONG),
                 ("reserve230", ULONG),
                 ("reserve231", ULONG),
                 ("reserve232", ULONG),
                 ("reserve233", ULONG),
                 ("reserve234", ULONG),
                 ("reserve235", ULONG),
                 ("reserve236", ULONG),
                 ("reserve237", ULONG),
                 ("reserve238", ULONG),
                 ("reserve239", ULONG),
                 ("reserve240", ULONG),
                 ("reserve241", ULONG),
                 ("reserve242", ULONG),
                 ("reserve243", ULONG),
                 ("reserve244", ULONG),
                 ("reserve245", ULONG),
                 ("reserve246", ULONG),
                 ("reserve247", ULONG),
                 ("reserve248", ULONG),
                 ("reserve249", ULONG),
                 ("reserve250", ULONG),
                 ("reserve251", ULONG),
                 ("reserve252", ULONG),
                 ("reserve253", ULONG),
                 ("reserve254", ULONG),
                 ("reserve255", ULONG),
                 ("reserve256", ULONG),
                 ("reserve257", ULONG),
                 ("reserve258", ULONG),
                 ("reserve259", ULONG),
                 ("reserve260", ULONG),
                 ("reserve261", ULONG),
                 ("reserve262", ULONG),
                 ("reserve263", ULONG),
                 ("reserve264", ULONG),
                 ("reserve265", ULONG),
                 ("reserve266", ULONG),
                 ("reserve267", ULONG),
                 ("reserve268", ULONG),
                 ("reserve269", ULONG),
                 ("reserve270", ULONG),
                 ("reserve271", ULONG),
                 ("reserve272", ULONG),
                 ("reserve273", ULONG),
                 ("reserve274", ULONG),
                 ("reserve275", ULONG),
                 ("reserve276", ULONG),
                 ("reserve277", ULONG),
                 ("reserve278", ULONG),
                 ("reserve279", ULONG),
                 ("reserve280", ULONG),
                 ("reserve281", ULONG),
                 ("reserve282", ULONG),
                 ("reserve283", ULONG),
                 ("reserve284", ULONG),
                 ("reserve285", ULONG),
                 ("reserve286", ULONG),
                 ("reserve287", ULONG),
                 ("reserve288", ULONG),
                 ("reserve289", ULONG),
                 ("reserve290", ULONG),
                 ("reserve291", ULONG),
                 ("reserve292", ULONG),
                 ("reserve293", ULONG),
                 ("reserve294", ULONG),
                 ("reserve295", ULONG),
                 ("reserve296", ULONG),
                 ("reserve297", ULONG),
                 ("reserve298", ULONG),
                 ("reserve299", ULONG),
                 ("reserve300", ULONG),
                 ("reserve301", ULONG),
                 ("reserve302", ULONG),
                 ("reserve303", ULONG),
                 ("reserve304", ULONG),
                 ("reserve305", ULONG),
                 ("reserve306", ULONG),
                 ("reserve307", ULONG),
                 ("reserve308", ULONG),
                 ("reserve309", ULONG),
                 ("reserve310", ULONG),
                 ("reserve311", ULONG),
                 ("reserve312", ULONG),
                 ("reserve313", ULONG),
                 ("reserve314", ULONG),
                 ("reserve315", ULONG),
                 ("reserve316", ULONG),
                 ("reserve317", ULONG),
                 ("reserve318", ULONG),
                 ("reserve319", ULONG),
                 ("reserve320", ULONG),
                 ("reserve321", ULONG),
                 ("reserve322", ULONG),
                 ("reserve323", ULONG),
                 ("reserve324", ULONG),
                 ("reserve325", ULONG),
                 ("reserve326", ULONG),
                 ("reserve327", ULONG),
                 ("reserve328", ULONG),
                 ("reserve329", ULONG),
                 ("reserve330", ULONG),
                 ("reserve331", ULONG),
                 ("reserve332", ULONG),
                 ("reserve333", ULONG),
                 ("reserve334", ULONG),
                 ("reserve335", ULONG),
                 ("reserve336", ULONG),
                 ("reserve337", ULONG),
                 ("reserve338", ULONG),
                 ("reserve339", ULONG),
                 ("reserve340", ULONG),
                 ("reserve341", ULONG),
                 ("reserve342", ULONG),
                 ("reserve343", ULONG),
                 ("reserve344", ULONG),
                 ("reserve345", ULONG)
                ]
class NtAlpcSendWaitReceivePort_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", BYTE*6),
                 ("reserve2", USHORT)
                ]
class NtAlpcSendWaitReceivePort_arg8_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtRemoveIoCompletion_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtRemoveIoCompletion_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtRemoveIoCompletion_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserValidateRect_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtUserRegisterRawInputDevices_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtCreateDirectoryObject_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtCreateDirectoryObject_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateDirectoryObject_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiGetCharacterPlacementW_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", c_char_p),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", POINTER(ULONG)),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", c_char_p),
                 ("reserve6", c_char_p),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG)
                ]
class NtGdiSetColorAdjustment_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", USHORT),
                 ("reserve6", USHORT),
                 ("reserve7", USHORT),
                 ("reserve8", USHORT),
                 ("reserve9", USHORT),
                 ("reserve10", USHORT),
                 ("reserve11", USHORT)
                ]
class NtGdiRectVisible_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtDeleteFile_arg1_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtDeleteFile_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtDeleteFile_arg1_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtCreateEvent_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtCreateEvent_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateEvent_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtQueryEaFile_arg2_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDIDestroyContext_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiXLATEOBJ_hGetColorTransform_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG),
                 ("reserve5", POINTER(ULONG))
                ]
class NtAddAtomEx_arg3_struct0(Structure):
     _fields_ = [("reserve0", USHORT)
                ]
class NtCreateWnfStateName_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtWaitForMultipleObjects_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtWaitForMultipleObjects_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiEngDeletePath_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtWriteFileGather_arg5_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtWriteFileGather_arg5_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtWriteFileGather_arg5_struct1),
                 ("reserve3", ULONG)
                )
class NtWriteFileGather_arg8_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtWriteFileGather_arg8_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtWriteFileGather_arg8_struct1),
                 ("reserve1", ULONG)
                )
class NtGdiDdDDIQueryRemoteVidPnSourceFromGdiDisplayName_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT*32),
                 ("reserve1", ULONG)
                ]
class NtUserGetKeyNameText_arg2_struct0(Structure):
     _fields_ = [("reserve0", c_char*2048)
                ]
class NtGdiGetTextExtent_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDICreateHwContext_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDICreateHwContext_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiDdDDICreateHwContext_arg1_struct1),
                 ("reserve4", ULONG),
                 ("reserve5", LPVOID),
                 ("reserve6", ULONG)
                ]
class NtGdiDdDDIInvalidateCache_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiResetDC_arg2_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT)
                ]

class NtGdiResetDC_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", c_char*64),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", ULONG),
                 ("reserve6", NtGdiResetDC_arg2_struct1),
                 ("reserve7", USHORT),
                 ("reserve8", USHORT),
                 ("reserve9", USHORT),
                 ("reserve10", USHORT),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT),
                 ("reserve13", USHORT),
                 ("reserve14", USHORT),
                 ("reserve15", USHORT),
                 ("reserve16", c_char*64),
                 ("reserve17", USHORT),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG),
                 ("reserve23", ULONG),
                 ("reserve24", ULONG),
                 ("reserve25", ULONG),
                 ("reserve26", ULONG),
                 ("reserve27", ULONG),
                 ("reserve28", ULONG),
                 ("reserve29", ULONG),
                 ("reserve30", ULONG)
                )
class NtGdiResetDC_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", c_char_p),
                 ("reserve2", c_char_p),
                 ("reserve3", c_char_p),
                 ("reserve4", c_char_p),
                 ("reserve5", c_char_p)
                ]
class NtUserCreateAcceleratorTable_arg1_struct0(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT)
                ]
class NtGdiDdDDIDestroyPagingQueue_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIGetContextSchedulingPriority_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserInitTask_arg4_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT)
                ]
class NtUserInitTask_arg5_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT)
                ]
class NtGdiDdDDIGetDeviceState_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]

class NtGdiDdDDIGetDeviceState_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDIGetDeviceState_arg1_struct2)
                )

class NtGdiDdDDIGetDeviceState_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiDdDDIGetDeviceState_arg1_struct1)
                )
class NtGdiDdDDIQueryVideoMemoryInfo_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG)
                ]
class NtQuerySymbolicLinkObject_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtQueryDefaultLocale_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateFile_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtCreateFile_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateFile_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtCreateFile_arg4_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDIOutputDuplGetPointerShapeData_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDIOutputDuplGetPointerShapeData_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiDdDDIOutputDuplGetPointerShapeData_arg1_struct2)
                )

class NtGdiDdDDIOutputDuplGetPointerShapeData_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", LPVOID),
                 ("reserve4", ULONG),
                 ("reserve5", NtGdiDdDDIOutputDuplGetPointerShapeData_arg1_struct1)
                )
class NtGdiHfontCreate_arg1_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG*16)
                ]

class NtGdiHfontCreate_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", BYTE),
                 ("reserve6", BYTE),
                 ("reserve7", BYTE),
                 ("reserve8", BYTE),
                 ("reserve9", BYTE),
                 ("reserve10", BYTE),
                 ("reserve11", BYTE),
                 ("reserve12", BYTE),
                 ("reserve13", c_char*2048)
                ]

class NtGdiHfontCreate_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiHfontCreate_arg1_struct2),
                 ("reserve1", c_char*128),
                 ("reserve2", c_char*64),
                 ("reserve3", c_char*2048)
                )

class NtGdiHfontCreate_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiHfontCreate_arg1_struct1),
                 ("reserve1", NtGdiHfontCreate_arg1_struct3)
                )
class NtGdiDdDDIPresentMultiPlaneOverlay2_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIPresentMultiPlaneOverlay2_arg1_struct6(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIPresentMultiPlaneOverlay2_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIPresentMultiPlaneOverlay2_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIPresentMultiPlaneOverlay2_arg1_struct7(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIPresentMultiPlaneOverlay2_arg1_struct3(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDIPresentMultiPlaneOverlay2_arg1_struct4),
                 ("reserve2", NtGdiDdDDIPresentMultiPlaneOverlay2_arg1_struct5),
                 ("reserve3", NtGdiDdDDIPresentMultiPlaneOverlay2_arg1_struct6),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", POINTER(NtGdiDdDDIPresentMultiPlaneOverlay2_arg1_struct7)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG)
                )

class NtGdiDdDDIPresentMultiPlaneOverlay2_arg1_struct2(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiDdDDIPresentMultiPlaneOverlay2_arg1_struct3)
                )

class NtGdiDdDDIPresentMultiPlaneOverlay2_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG*64),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", NtGdiDdDDIPresentMultiPlaneOverlay2_arg1_struct1),
                 ("reserve8", ULONG),
                 ("reserve9", POINTER(NtGdiDdDDIPresentMultiPlaneOverlay2_arg1_struct2)),
                 ("reserve10", ULONG)
                )
class NtGdiDdDDIPresentMultiPlaneOverlay3_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIPresentMultiPlaneOverlay3_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIPresentMultiPlaneOverlay3_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDIPresentMultiPlaneOverlay3_arg1_struct3(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIPresentMultiPlaneOverlay3_arg1_struct2(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiDdDDIPresentMultiPlaneOverlay3_arg1_struct3),
                 ("reserve1", NtGdiDdDDIPresentMultiPlaneOverlay3_arg1_struct4),
                 ("reserve2", NtGdiDdDDIPresentMultiPlaneOverlay3_arg1_struct5),
                 ("reserve3", ULONG)
                )

class NtGdiDdDDIPresentMultiPlaneOverlay3_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", LPVOID),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", NtGdiDdDDIPresentMultiPlaneOverlay3_arg1_struct1),
                 ("reserve6", ULONG),
                 ("reserve7", LPVOID),
                 ("reserve8", POINTER(NtGdiDdDDIPresentMultiPlaneOverlay3_arg1_struct2)),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", LPVOID)
                ]
class NtFilterToken_arg3_struct3(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtFilterToken_arg3_struct2(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtFilterToken_arg3_struct3),
                 ("reserve3", ULONG*1024)
                ]

class NtFilterToken_arg3_struct1(ctypes.Structure):
     _fields_ = (("reserve0", POINTER(NtFilterToken_arg3_struct2)),
                 ("reserve1", ULONG)
                )

class NtFilterToken_arg3_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtFilterToken_arg3_struct1*512)
                )
class NtFilterToken_arg4_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtFilterToken_arg4_struct1(ctypes.Structure):
     _fields_ = (("reserve0", NtFilterToken_arg4_struct2),
                 ("reserve1", ULONG)
                )

class NtFilterToken_arg4_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtFilterToken_arg4_struct1*341)
                )
class NtFilterToken_arg5_struct3(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtFilterToken_arg5_struct2(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtFilterToken_arg5_struct3),
                 ("reserve3", ULONG*1024)
                ]

class NtFilterToken_arg5_struct1(ctypes.Structure):
     _fields_ = (("reserve0", POINTER(NtFilterToken_arg5_struct2)),
                 ("reserve1", ULONG)
                )

class NtFilterToken_arg5_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtFilterToken_arg5_struct1*512)
                )
class NtDeviceIoControlFile_arg5_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtWaitForKeyedEvent_arg2_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG))
                ]
class NtGdiDdDDIOpenAdapterFromHdc_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDIOpenAdapterFromHdc_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiDdDDIOpenAdapterFromHdc_arg1_struct1),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG)
                )
class NtGdiDdDDIGetAllocationPriority_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG))
                ]
class NtSetInformationWorkerFactory_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDICreateDCFromMemory_arg1_struct1(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE)
                ]

class NtGdiDdDDICreateDCFromMemory_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", POINTER(NtGdiDdDDICreateDCFromMemory_arg1_struct1)),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG)
                )
class NtGdiSetBrushOrg_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtLoadKey_arg1_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtLoadKey_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtLoadKey_arg1_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                )
class NtLoadKey_arg2_struct2(Structure):
     _fields_ = [("reserve0", c_char*2048)
                ]

class NtLoadKey_arg2_struct1(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtLoadKey_arg2_struct2))
                )

class NtLoadKey_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtLoadKey_arg2_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                )
class NtUserOpenDesktop_arg1_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtUserOpenDesktop_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtUserOpenDesktop_arg1_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                )
class NtUserGetRawPointerDeviceData_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", USHORT),
                 ("reserve7", USHORT)
                ]
class NtGetCompleteWnfStateSubscription_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGetCompleteWnfStateSubscription_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserMagGetContextInformation_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiExtTextOutW_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiDdDDIQueryFSEBlock_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDIQueryFSEBlock_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtGdiDdDDIQueryFSEBlock_arg1_struct1),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                )
class NtGdiDdDDIDestroyAllocation_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", ULONG)
                ]
class NtUserClipCursor_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiDdDDIDestroySynchronizationObject_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetKeyboardLayoutName_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGdiDdDDICreateKeyedMutex2_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDICreateKeyedMutex2_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", POINTER(ULONG)),
                 ("reserve4", ULONG),
                 ("reserve5", NtGdiDdDDICreateKeyedMutex2_arg1_struct1)
                )
class NtNotifyChangeKey_arg5_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtUserThunkedMenuItemInfo_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserThunkedMenuItemInfo_arg6_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGdiDdDDIUpdateAllocationProperty_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIUpdateAllocationProperty_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIUpdateAllocationProperty_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiDdDDIUpdateAllocationProperty_arg1_struct1),
                 ("reserve4", NtGdiDdDDIUpdateAllocationProperty_arg1_struct2),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG)
                )
class NtGdiStretchDIBitsInternal_arg11_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG)
                ]

class NtGdiStretchDIBitsInternal_arg11_struct0(Structure):
     _fields_ = [("reserve0", NtGdiStretchDIBitsInternal_arg11_struct1),
                 ("reserve1", ULONG*1)
                ]
class NtWaitForWorkViaWorkerFactory_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtWaitForWorkViaWorkerFactory_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtWaitForWorkViaWorkerFactory_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtGdiXFORMOBJ_iGetXform_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiXFORMOBJ_iGetXform_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]
class NtGdiScaleViewportExtEx_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDIGetResourcePresentPrivateDriverData_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG))
                ]
class NtGdiDdDDIDestroyDCFromMemory_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtCreateResourceManager_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]
class NtCreateResourceManager_arg5_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtCreateResourceManager_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateResourceManager_arg5_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtCreateResourceManager_arg7_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtPrivilegedServiceAuditAlarm_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtPrivilegedServiceAuditAlarm_arg2_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtPrivilegedServiceAuditAlarm_arg4_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtPrivilegedServiceAuditAlarm_arg4_struct1(ctypes.Structure):
     _fields_ = (("reserve0", NtPrivilegedServiceAuditAlarm_arg4_struct2),
                 ("reserve1", ULONG)
                )

class NtPrivilegedServiceAuditAlarm_arg4_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtPrivilegedServiceAuditAlarm_arg4_struct1*341)
                )
class NtOpenKeyTransacted_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenKeyTransacted_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenKeyTransacted_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtUserGetGestureExtArgs_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtVdmControl_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtQueryDirectoryFile_arg5_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtQueryDirectoryFile_arg10_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGdiDdDDIFreeGpuVirtualAddress_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtGdiGetRasterizerCaps_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT)
                ]
class NtUserDispatchMessage_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserDispatchMessage_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(ULONG)),
                 ("reserve3", POINTER(ULONG)),
                 ("reserve4", ULONG),
                 ("reserve5", NtUserDispatchMessage_arg1_struct1),
                 ("reserve6", ULONG)
                )
class NtUserEnumDisplayDevices_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG)
                ]
class NtUserGetOemBitmapSize_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDITrimProcessCommitment_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG)
                ]
class NtGdiEngPaint_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiEngPaint_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiEngPaint_arg1_struct1),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", POINTER(ULONG)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", USHORT),
                 ("reserve12", USHORT)
                ]
class NtGdiEngPaint_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiEngPaint_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiEngPaint_arg2_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtGdiEngPaint_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtGdiEngPaint_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtOpenTransactionManager_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtOpenTransactionManager_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtOpenTransactionManager_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtOpenTransactionManager_arg4_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtOpenTransactionManager_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]
class NtGdiHT_Get8BPPMaskPalette_arg1_struct0(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE)
                ]
class NtGdiDdDDICheckMultiPlaneOverlaySupport3_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDICheckMultiPlaneOverlaySupport3_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", LPVOID),
                 ("reserve4", ULONG),
                 ("reserve5", LPVOID),
                 ("reserve6", ULONG),
                 ("reserve7", NtGdiDdDDICheckMultiPlaneOverlaySupport3_arg1_struct1)
                )
class NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct8(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct6(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct7(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct3(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct4),
                 ("reserve2", NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct5),
                 ("reserve3", NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct6),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", POINTER(NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct7)),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG)
                )

class NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct2),
                 ("reserve3", ULONG),
                 ("reserve4", NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct3)
                )

class NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", POINTER(NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct1)),
                 ("reserve4", ULONG),
                 ("reserve5", NtGdiDdDDICheckMultiPlaneOverlaySupport2_arg1_struct8)
                )
class NtGetContextThread_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiDdDDIQueryProtectedSessionStatus_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtUserTrackMouseEvent_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtQueueApcThread_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtAccessCheckByTypeResultList_arg1_struct2(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckByTypeResultList_arg1_struct1(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckByTypeResultList_arg1_struct2),
                 ("reserve3", ULONG*1024)
                ]

class NtAccessCheckByTypeResultList_arg1_struct4(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckByTypeResultList_arg1_struct3(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckByTypeResultList_arg1_struct4),
                 ("reserve3", ULONG*1024)
                ]

class NtAccessCheckByTypeResultList_arg1_struct5(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtAccessCheckByTypeResultList_arg1_struct6(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", USHORT)
                ]

class NtAccessCheckByTypeResultList_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", POINTER(NtAccessCheckByTypeResultList_arg1_struct1)),
                 ("reserve4", POINTER(NtAccessCheckByTypeResultList_arg1_struct3)),
                 ("reserve5", POINTER(NtAccessCheckByTypeResultList_arg1_struct5)),
                 ("reserve6", POINTER(NtAccessCheckByTypeResultList_arg1_struct6))
                )
class NtAccessCheckByTypeResultList_arg2_struct1(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtAccessCheckByTypeResultList_arg2_struct0(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtAccessCheckByTypeResultList_arg2_struct1),
                 ("reserve3", ULONG*1024)
                ]
class NtAccessCheckByTypeResultList_arg5_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", BYTE*8)
                ]

class NtAccessCheckByTypeResultList_arg5_struct0(ctypes.Structure):
     _fields_ = (("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", POINTER(NtAccessCheckByTypeResultList_arg5_struct1))
                )
class NtAccessCheckByTypeResultList_arg7_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtAccessCheckByTypeResultList_arg8_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtAccessCheckByTypeResultList_arg8_struct1(ctypes.Structure):
     _fields_ = (("reserve0", NtAccessCheckByTypeResultList_arg8_struct2),
                 ("reserve1", ULONG)
                )

class NtAccessCheckByTypeResultList_arg8_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtAccessCheckByTypeResultList_arg8_struct1*341)
                )
class NtGdiDdDDINetDispStartMiracastDisplayDevice_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", USHORT),
                 ("reserve2", USHORT),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG),
                 ("reserve23", ULONG),
                 ("reserve24", ULONG),
                 ("reserve25", ULONG),
                 ("reserve26", ULONG),
                 ("reserve27", ULONG),
                 ("reserve28", ULONG),
                 ("reserve29", ULONG),
                 ("reserve30", ULONG),
                 ("reserve31", ULONG),
                 ("reserve32", ULONG),
                 ("reserve33", ULONG),
                 ("reserve34", ULONG),
                 ("reserve35", ULONG),
                 ("reserve36", ULONG),
                 ("reserve37", ULONG),
                 ("reserve38", ULONG),
                 ("reserve39", ULONG),
                 ("reserve40", ULONG),
                 ("reserve41", ULONG),
                 ("reserve42", ULONG),
                 ("reserve43", ULONG),
                 ("reserve44", ULONG),
                 ("reserve45", ULONG),
                 ("reserve46", ULONG),
                 ("reserve47", ULONG),
                 ("reserve48", ULONG),
                 ("reserve49", ULONG),
                 ("reserve50", ULONG),
                 ("reserve51", ULONG),
                 ("reserve52", ULONG),
                 ("reserve53", ULONG),
                 ("reserve54", ULONG),
                 ("reserve55", ULONG),
                 ("reserve56", ULONG),
                 ("reserve57", ULONG),
                 ("reserve58", ULONG),
                 ("reserve59", ULONG),
                 ("reserve60", ULONG),
                 ("reserve61", ULONG),
                 ("reserve62", ULONG),
                 ("reserve63", ULONG),
                 ("reserve64", ULONG),
                 ("reserve65", ULONG),
                 ("reserve66", ULONG),
                 ("reserve67", ULONG),
                 ("reserve68", ULONG),
                 ("reserve69", ULONG),
                 ("reserve70", ULONG),
                 ("reserve71", ULONG),
                 ("reserve72", ULONG),
                 ("reserve73", ULONG),
                 ("reserve74", ULONG),
                 ("reserve75", ULONG),
                 ("reserve76", ULONG),
                 ("reserve77", ULONG),
                 ("reserve78", ULONG),
                 ("reserve79", ULONG),
                 ("reserve80", ULONG),
                 ("reserve81", ULONG),
                 ("reserve82", ULONG),
                 ("reserve83", ULONG),
                 ("reserve84", ULONG),
                 ("reserve85", ULONG),
                 ("reserve86", ULONG),
                 ("reserve87", ULONG),
                 ("reserve88", ULONG),
                 ("reserve89", ULONG),
                 ("reserve90", ULONG),
                 ("reserve91", ULONG),
                 ("reserve92", ULONG),
                 ("reserve93", ULONG),
                 ("reserve94", ULONG),
                 ("reserve95", ULONG),
                 ("reserve96", ULONG),
                 ("reserve97", ULONG),
                 ("reserve98", ULONG),
                 ("reserve99", ULONG),
                 ("reserve100", ULONG),
                 ("reserve101", ULONG),
                 ("reserve102", ULONG),
                 ("reserve103", ULONG),
                 ("reserve104", ULONG),
                 ("reserve105", ULONG),
                 ("reserve106", ULONG),
                 ("reserve107", ULONG),
                 ("reserve108", ULONG),
                 ("reserve109", ULONG),
                 ("reserve110", ULONG),
                 ("reserve111", ULONG),
                 ("reserve112", ULONG),
                 ("reserve113", ULONG),
                 ("reserve114", ULONG),
                 ("reserve115", ULONG),
                 ("reserve116", ULONG),
                 ("reserve117", ULONG),
                 ("reserve118", ULONG),
                 ("reserve119", ULONG),
                 ("reserve120", ULONG),
                 ("reserve121", ULONG),
                 ("reserve122", ULONG),
                 ("reserve123", ULONG),
                 ("reserve124", ULONG),
                 ("reserve125", ULONG),
                 ("reserve126", ULONG),
                 ("reserve127", ULONG),
                 ("reserve128", ULONG),
                 ("reserve129", ULONG),
                 ("reserve130", ULONG),
                 ("reserve131", ULONG),
                 ("reserve132", ULONG),
                 ("reserve133", ULONG),
                 ("reserve134", ULONG),
                 ("reserve135", ULONG),
                 ("reserve136", ULONG),
                 ("reserve137", ULONG)
                ]
class NtNotifyChangeDirectoryFile_arg5_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtNotifyChangeDirectoryFile_arg6_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiGetDeviceCapsAll_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG)
                ]
class NtUserBuildPropList_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserBuildPropList_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetCursorFrameInfo_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetCursorFrameInfo_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserGetWindowPlacement_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateEnclave_arg2_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG))
                ]
class NtCreateLowBoxToken_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtCreateLowBoxToken_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", USHORT),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", USHORT)
                ]
class NtCreateLowBoxToken_arg5_struct1(Structure):
     _fields_ = [("reserve0", BYTE*6)
                ]

class NtCreateLowBoxToken_arg5_struct0(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", NtCreateLowBoxToken_arg5_struct1),
                 ("reserve3", ULONG*1024)
                ]
class NtCreateLowBoxToken_arg7_struct1(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE),
                 ("reserve2", USHORT),
                 ("reserve3", USHORT),
                 ("reserve4", ULONG)
                ]

class NtCreateLowBoxToken_arg7_struct0(ctypes.Structure):
     _fields_ = (("reserve0", POINTER(NtCreateLowBoxToken_arg7_struct1)),
                 ("reserve1", ULONG)
                )
class NtCreateLowBoxToken_arg9_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG)
                ]
class NtGdiDdDDICheckSharedResourceAccess_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtSetContextThread_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", BYTE*80),
                 ("reserve8", ULONG)
                ]

class NtSetContextThread_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", NtSetContextThread_arg2_struct1),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG),
                 ("reserve23", ULONG),
                 ("reserve24", BYTE*512)
                ]
class NtUserGetPointerInfoList_arg8_struct5(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserGetPointerInfoList_arg8_struct4(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserGetPointerInfoList_arg8_struct3(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserGetPointerInfoList_arg8_struct2(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtUserGetPointerInfoList_arg8_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", NtUserGetPointerInfoList_arg8_struct2),
                 ("reserve7", NtUserGetPointerInfoList_arg8_struct3),
                 ("reserve8", NtUserGetPointerInfoList_arg8_struct4),
                 ("reserve9", NtUserGetPointerInfoList_arg8_struct5),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG)
                )

class NtUserGetPointerInfoList_arg8_struct0(ctypes.Structure):
     _fields_ = (("reserve0", NtUserGetPointerInfoList_arg8_struct1),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                )
class NtSetInformationVirtualMemory_arg4_struct0(Structure):
     _fields_ = [("reserve0", POINTER(ULONG)),
                 ("reserve1", ULONG)
                ]
class NtSetInformationObject_arg3_struct0(Structure):
     _fields_ = [("reserve0", BYTE),
                 ("reserve1", BYTE)
                ]
class NtGdiDdDDICheckMonitorPowerState_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiDdDDICreateSynchronizationObject_arg1_struct3(Structure):
     _fields_ = [("reserve0", c_longlong*8)
                ]

class NtGdiDdDDICreateSynchronizationObject_arg1_struct2(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDICreateSynchronizationObject_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDICreateSynchronizationObject_arg1_struct2),
                 ("reserve2", NtGdiDdDDICreateSynchronizationObject_arg1_struct3),
                 ("reserve3", ULONG)
                )

class NtGdiDdDDICreateSynchronizationObject_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", NtGdiDdDDICreateSynchronizationObject_arg1_struct1),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG),
                 ("reserve11", ULONG),
                 ("reserve12", ULONG),
                 ("reserve13", ULONG),
                 ("reserve14", ULONG),
                 ("reserve15", ULONG),
                 ("reserve16", ULONG),
                 ("reserve17", ULONG),
                 ("reserve18", ULONG),
                 ("reserve19", ULONG),
                 ("reserve20", ULONG),
                 ("reserve21", ULONG),
                 ("reserve22", ULONG)
                )
class NtQueryWnfStateNameInformation_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtQueryWnfStateNameInformation_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtGdiGetBoundsRect_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtGdiDdDDIUpdateGpuVirtualAddress_arg1_struct3(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDIUpdateGpuVirtualAddress_arg1_struct2(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", ULONG),
                 ("reserve5", NtGdiDdDDIUpdateGpuVirtualAddress_arg1_struct3),
                 ("reserve6", ULONG)
                )

class NtGdiDdDDIUpdateGpuVirtualAddress_arg1_struct1(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiDdDDIUpdateGpuVirtualAddress_arg1_struct2)
                )

class NtGdiDdDDIUpdateGpuVirtualAddress_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(NtGdiDdDDIUpdateGpuVirtualAddress_arg1_struct1)),
                 ("reserve5", ULONG),
                 ("reserve6", ULONG),
                 ("reserve7", ULONG),
                 ("reserve8", ULONG)
                )
class NtGdiDdDDIQueryVidPnExclusiveOwnership_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiDdDDIQueryVidPnExclusiveOwnership_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", NtGdiDdDDIQueryVidPnExclusiveOwnership_arg1_struct1),
                 ("reserve4", ULONG)
                )
class NtGdiPATHOBJ_bEnum_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiPATHOBJ_bEnum_arg2_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]

class NtGdiPATHOBJ_bEnum_arg2_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtGdiPATHOBJ_bEnum_arg2_struct1))
                )
class NtGdiDoBanding_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiDoBanding_arg4_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiBRUSHOBJ_pvGetRbrush_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]
class NtGdiCLIPOBJ_ppoGetPath_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]

class NtGdiCLIPOBJ_ppoGetPath_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", NtGdiCLIPOBJ_ppoGetPath_arg1_struct1),
                 ("reserve2", BYTE),
                 ("reserve3", BYTE),
                 ("reserve4", BYTE),
                 ("reserve5", BYTE)
                )
class NtQueryTimerResolution_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtQueryTimerResolution_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtQueryTimerResolution_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG)
                ]
class NtUserRegisterWindowMessage_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
class NtGdiDdDDISignalSynchronizationObjectFromCpu_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG)
                ]

class NtGdiDdDDISignalSynchronizationObjectFromCpu_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", LPVOID),
                 ("reserve3", LPVOID),
                 ("reserve4", NtGdiDdDDISignalSynchronizationObjectFromCpu_arg1_struct1)
                )
class NtGdiPATHOBJ_vGetBounds_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG)
                ]
class NtGdiPATHOBJ_vGetBounds_arg2_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", ULONG)
                ]
class NtCreateSection_arg3_struct1(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtCreateSection_arg3_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtCreateSection_arg3_struct1)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]
class NtGdiDdDDIOpenSyncObjectNtHandleFromName_arg1_struct2(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]

class NtGdiDdDDIOpenSyncObjectNtHandleFromName_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", POINTER(NtGdiDdDDIOpenSyncObjectNtHandleFromName_arg1_struct2)),
                 ("reserve3", ULONG),
                 ("reserve4", POINTER(ULONG)),
                 ("reserve5", POINTER(ULONG))
                ]

class NtGdiDdDDIOpenSyncObjectNtHandleFromName_arg1_struct0(ctypes.Structure):
     _fields_ = (("reserve0", ULONG),
                 ("reserve1", POINTER(NtGdiDdDDIOpenSyncObjectNtHandleFromName_arg1_struct1)),
                 ("reserve2", ULONG)
                )
class NtGdiDdDDIOpenResource_arg1_struct1(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", POINTER(ULONG)),
                 ("reserve2", ULONG)
                ]

class NtGdiDdDDIOpenResource_arg1_struct0(Structure):
     _fields_ = [("reserve0", ULONG),
                 ("reserve1", ULONG),
                 ("reserve2", ULONG),
                 ("reserve3", LPVOID),
                 ("reserve4", LPVOID),
                 ("reserve5", ULONG),
                 ("reserve6", LPVOID),
                 ("reserve7", ULONG),
                 ("reserve8", LPVOID),
                 ("reserve9", ULONG),
                 ("reserve10", ULONG)
                ]
class NtCloseObjectAuditAlarm_arg1_struct0(Structure):
     _fields_ = [("reserve0", USHORT),
                 ("reserve1", USHORT),
                 ("reserve2", c_char_p)
                ]
