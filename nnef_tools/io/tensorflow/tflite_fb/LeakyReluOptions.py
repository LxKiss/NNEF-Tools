# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_fb

import flatbuffers

class LeakyReluOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsLeakyReluOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LeakyReluOptions()
        x.Init(buf, n + offset)
        return x

    # LeakyReluOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # LeakyReluOptions
    def Alpha(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def LeakyReluOptionsStart(builder): builder.StartObject(1)
def LeakyReluOptionsAddAlpha(builder, alpha): builder.PrependFloat32Slot(0, alpha, 0.0)
def LeakyReluOptionsEnd(builder): return builder.EndObject()
