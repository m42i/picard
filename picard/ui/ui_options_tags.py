# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\options_tags.ui'
#
# Created: Mon Jun 03 12:50:08 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TagsOptionsPage(object):
    def setupUi(self, TagsOptionsPage):
        TagsOptionsPage.setObjectName(_fromUtf8("TagsOptionsPage"))
        TagsOptionsPage.resize(539, 425)
        self.vboxlayout = QtGui.QVBoxLayout(TagsOptionsPage)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.write_tags = QtGui.QCheckBox(TagsOptionsPage)
        self.write_tags.setObjectName(_fromUtf8("write_tags"))
        self.vboxlayout.addWidget(self.write_tags)
        self.preserve_timestamps = QtGui.QCheckBox(TagsOptionsPage)
        self.preserve_timestamps.setObjectName(_fromUtf8("preserve_timestamps"))
        self.vboxlayout.addWidget(self.preserve_timestamps)
        self.before_tagging = QtGui.QGroupBox(TagsOptionsPage)
        self.before_tagging.setObjectName(_fromUtf8("before_tagging"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.before_tagging)
        self.vboxlayout1.setSpacing(2)
        self.vboxlayout1.setContentsMargins(-1, 6, -1, 7)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.clear_existing_tags = QtGui.QCheckBox(self.before_tagging)
        self.clear_existing_tags.setObjectName(_fromUtf8("clear_existing_tags"))
        self.vboxlayout1.addWidget(self.clear_existing_tags)
        self.remove_id3_from_flac = QtGui.QCheckBox(self.before_tagging)
        self.remove_id3_from_flac.setObjectName(_fromUtf8("remove_id3_from_flac"))
        self.vboxlayout1.addWidget(self.remove_id3_from_flac)
        self.remove_ape_from_mp3 = QtGui.QCheckBox(self.before_tagging)
        self.remove_ape_from_mp3.setObjectName(_fromUtf8("remove_ape_from_mp3"))
        self.vboxlayout1.addWidget(self.remove_ape_from_mp3)
        spacerItem = QtGui.QSpacerItem(20, 6, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.vboxlayout1.addItem(spacerItem)
        self.preserved_tags_label = QtGui.QLabel(self.before_tagging)
        self.preserved_tags_label.setObjectName(_fromUtf8("preserved_tags_label"))
        self.vboxlayout1.addWidget(self.preserved_tags_label)
        self.preserved_tags = QtGui.QLineEdit(self.before_tagging)
        self.preserved_tags.setObjectName(_fromUtf8("preserved_tags"))
        self.vboxlayout1.addWidget(self.preserved_tags)
        self.preserved_tags_help = QtGui.QLabel(self.before_tagging)
        self.preserved_tags_help.setObjectName(_fromUtf8("preserved_tags_help"))
        self.vboxlayout1.addWidget(self.preserved_tags_help)
        self.vboxlayout.addWidget(self.before_tagging)
        self.tag_compatibility = QtGui.QGroupBox(TagsOptionsPage)
        self.tag_compatibility.setObjectName(_fromUtf8("tag_compatibility"))
        self.vboxlayout2 = QtGui.QVBoxLayout(self.tag_compatibility)
        self.preserve_coverimage = QtGui.QCheckBox(self.rename_files)
        self.preserve_coverimage.setObjectName(_fromUtf8("preserve_coverimage"))
        self.vboxlayout1.addWidget(self.preserve_coverimage)
        self.vboxlayout2.setSpacing(2)
        self.vboxlayout2.setContentsMargins(-1, 6, -1, 7)
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.id3v2_version = QtGui.QGroupBox(self.tag_compatibility)
        self.id3v2_version.setFlat(False)
        self.id3v2_version.setCheckable(False)
        self.id3v2_version.setObjectName(_fromUtf8("id3v2_version"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.id3v2_version)
        self.horizontalLayout.setContentsMargins(-1, 6, -1, 7)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.write_id3v24 = QtGui.QRadioButton(self.id3v2_version)
        self.write_id3v24.setChecked(True)
        self.write_id3v24.setObjectName(_fromUtf8("write_id3v24"))
        self.horizontalLayout.addWidget(self.write_id3v24)
        self.write_id3v23 = QtGui.QRadioButton(self.id3v2_version)
        self.write_id3v23.setChecked(False)
        self.write_id3v23.setObjectName(_fromUtf8("write_id3v23"))
        self.horizontalLayout.addWidget(self.write_id3v23)
        self.label = QtGui.QLabel(self.id3v2_version)
        self.label.setText(_fromUtf8(""))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.vboxlayout2.addWidget(self.id3v2_version)
        self.id3v2_text_encoding = QtGui.QGroupBox(self.tag_compatibility)
        self.id3v2_text_encoding.setObjectName(_fromUtf8("id3v2_text_encoding"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.id3v2_text_encoding)
        self.horizontalLayout_2.setContentsMargins(-1, 6, -1, 7)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.enc_utf8 = QtGui.QRadioButton(self.id3v2_text_encoding)
        self.enc_utf8.setObjectName(_fromUtf8("enc_utf8"))
        self.horizontalLayout_2.addWidget(self.enc_utf8)
        self.enc_utf16 = QtGui.QRadioButton(self.id3v2_text_encoding)
        self.enc_utf16.setObjectName(_fromUtf8("enc_utf16"))
        self.horizontalLayout_2.addWidget(self.enc_utf16)
        self.enc_iso88591 = QtGui.QRadioButton(self.id3v2_text_encoding)
        self.enc_iso88591.setObjectName(_fromUtf8("enc_iso88591"))
        self.horizontalLayout_2.addWidget(self.enc_iso88591)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2 = QtGui.QLabel(self.id3v2_text_encoding)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.vboxlayout2.addWidget(self.id3v2_text_encoding)
        self.hbox_id3v23_join_with = QtGui.QHBoxLayout()
        self.hbox_id3v23_join_with.setObjectName(_fromUtf8("hbox_id3v23_join_with"))
        self.label_id3v23_join_with = QtGui.QLabel(self.tag_compatibility)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_id3v23_join_with.sizePolicy().hasHeightForWidth())
        self.label_id3v23_join_with.setSizePolicy(sizePolicy)
        self.label_id3v23_join_with.setObjectName(_fromUtf8("label_id3v23_join_with"))
        self.hbox_id3v23_join_with.addWidget(self.label_id3v23_join_with)
        self.id3v23_join_with = QtGui.QComboBox(self.tag_compatibility)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.id3v23_join_with.sizePolicy().hasHeightForWidth())
        self.id3v23_join_with.setSizePolicy(sizePolicy)
        self.id3v23_join_with.setEditable(True)
        self.id3v23_join_with.setObjectName(_fromUtf8("id3v23_join_with"))
        self.id3v23_join_with.addItem(_fromUtf8(""))
        self.id3v23_join_with.setItemText(0, _fromUtf8("/"))
        self.id3v23_join_with.addItem(_fromUtf8(""))
        self.id3v23_join_with.setItemText(1, _fromUtf8("; "))
        self.id3v23_join_with.addItem(_fromUtf8(""))
        self.id3v23_join_with.setItemText(2, _fromUtf8(" / "))
        self.hbox_id3v23_join_with.addWidget(self.id3v23_join_with)
        self.vboxlayout2.addLayout(self.hbox_id3v23_join_with)
        self.write_id3v1 = QtGui.QCheckBox(self.tag_compatibility)
        self.write_id3v1.setObjectName(_fromUtf8("write_id3v1"))
        self.vboxlayout2.addWidget(self.write_id3v1)
        self.vboxlayout.addWidget(self.tag_compatibility)
        spacerItem3 = QtGui.QSpacerItem(274, 41, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem3)

        self.retranslateUi(TagsOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(TagsOptionsPage)
        TagsOptionsPage.setTabOrder(self.write_tags, self.preserve_timestamps)
        TagsOptionsPage.setTabOrder(self.preserve_timestamps, self.clear_existing_tags)
        TagsOptionsPage.setTabOrder(self.clear_existing_tags, self.remove_id3_from_flac)
        TagsOptionsPage.setTabOrder(self.remove_id3_from_flac, self.remove_ape_from_mp3)
        TagsOptionsPage.setTabOrder(self.remove_ape_from_mp3, self.preserved_tags)
        TagsOptionsPage.setTabOrder(self.preserved_tags, self.write_id3v24)
        TagsOptionsPage.setTabOrder(self.write_id3v24, self.write_id3v23)
        TagsOptionsPage.setTabOrder(self.write_id3v23, self.enc_utf8)
        TagsOptionsPage.setTabOrder(self.enc_utf8, self.enc_utf16)
        TagsOptionsPage.setTabOrder(self.enc_utf16, self.enc_iso88591)
        TagsOptionsPage.setTabOrder(self.enc_iso88591, self.id3v23_join_with)
        TagsOptionsPage.setTabOrder(self.id3v23_join_with, self.write_id3v1)

    def retranslateUi(self, TagsOptionsPage):
        self.write_tags.setText(_("Write tags to files"))
        self.preserve_timestamps.setText(_("Preserve timestamps of tagged files"))
        self.before_tagging.setTitle(_("Before Tagging"))
        self.clear_existing_tags.setText(_("Clear existing tags"))
        self.remove_id3_from_flac.setText(_("Remove ID3 tags from FLAC files"))
        self.remove_ape_from_mp3.setText(_("Remove APEv2 tags from MP3 files"))
        self.preserved_tags_label.setText(_("Preserve these tags from being cleared or overwritten with MusicBrainz data:"))
        self.preserved_tags_help.setText(_("Tags are separated by commas, and are case-sensitive."))
        self.tag_compatibility.setTitle(_("Tag Compatibility"))
        self.id3v2_version.setTitle(_("ID3v2 Version"))
        self.preserved_tags_help.setText(_("Tags are separated by spaces, and are case-sensitive."))
        self.preserve_coverimage.setText(_("Preserve cover images when clearing tags. This ignores the embed cover art option."))
        self.write_id3v24.setText(_("2.4"))
        self.write_id3v23.setText(_("2.3"))
        self.id3v2_text_encoding.setTitle(_("ID3v2 Text Encoding"))
        self.enc_utf8.setText(_("UTF-8"))
        self.enc_utf16.setText(_("UTF-16"))
        self.enc_iso88591.setText(_("ISO-8859-1"))
        self.label_id3v23_join_with.setText(_("Join multiple ID3v2.3 tags with:"))
        self.id3v23_join_with.setToolTip(_("<html><head/><body><p>Default is \'/\' to maintain compatibility with previous Picard releases.</p><p>New alternatives are \';_\' or \'_/_\' or type your own. </p></body></html>"))
        self.write_id3v1.setText(_("Also include ID3v1 tags in the files"))

