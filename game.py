class Game:
    name = ''
    downloadUrl = ''
    pkName = ''
    versionName = ''
    downloadCount = -1
    file_md5 = ''

    def _init__(self):
        self.name = ''
        self.downloadCount = ''
        self.downloadUrl = ''
        self.file_md5 = ''
        self.versionName = ''
        self.pkName = ''
        self.rank = ''

    def __init__(self, rank,name, downloadUrl, downloadCount, file_md5, pkName, versionName) -> None:
        self.name = name
        self.downloadCount = downloadCount
        self.downloadUrl = downloadUrl
        self.file_md5 = file_md5
        self.versionName = versionName
        self.pkName = pkName
        self.rank = rank
