from dearpygui.core import *
from dearpygui.simple import *

import webbrowser

from src.backend.web import *

from src.ui.UI import *



class UsedLibs:
    @staticmethod
    def close_libs():
        close_popup('Used libraries')

    """
    Functions to open links to the listed libraries
    """

    @staticmethod
    def dearpygui():
        webbrowser.open(URL.github + 'hoffstadt/dearpygui')

    @staticmethod
    def pypresence():
        webbrowser.open(URL.github + 'qwertyquerty/pypresence')

    @staticmethod
    def lxml():
        webbrowser.open(URL.github + 'lxml/lxml')

    @staticmethod
    def requests():
        webbrowser.open(URL.github + 'psf/requests')

    @staticmethod
    def pillow():
        webbrowser.open(URL.github + 'python-pillow/pillow')

    @staticmethod
    def pywin32():
        webbrowser.open(URL.github + 'mhammond/pywin32')

    """
    Show all used libraries with their license and GitHub link
    """

    @staticmethod
    def show():
        add_text('Dear PyGui')

        add_text('MIT License\n'
                 '\n'
                 'Copyright (c) 2020 Raylock, LLC\n'
                 '\n'
                 'Permission is hereby granted, free of charge, to any \nperson obtaining a copy\n'
                 'of this software and associated documentation files \n(the "Software"), to deal\n'
                 'in the Software without restriction, including without \nlimitation the rights\n'
                 'to use, copy, modify, merge, publish, distribute, sublicense, \nand/or sell\n'
                 'copies of the Software, and to permit persons to whom the \nSoftware is\n'
                 'furnished to do so, subject to the following conditions:\n'
                 '\n'
                 'The above copyright notice and this permission notice shall be \nincluded in all\n'
                 'copies or substantial portions of the Software.\n'
                 '\n'
                 'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY \nKIND, EXPRESS OR\n'
                 'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF \nMERCHANTABILITY,\n'
                 'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN \nNO EVENT SHALL THE\n'
                 'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, \nDAMAGES OR OTHER\n'
                 'LIABILITY, WHETHER IN AN ACTION OF CONTRACT, \n'
                 'TORT OR OTHERWISE, ARISING FROM,\n'
                 'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE \n'
                 'USE OR OTHER DEALINGS IN THE\n'
                 'SOFTWARE.\n')

        Buttons.create('UsedLibs_GitHub_DearPyGui', 'SMALL', 'GitHub', UsedLibs.dearpygui)

        add_separator()

        add_text('pypresence')

        add_text('MIT License\n'
                 '\n'
                 'Copyright (c) 2018 qwertyquerty\n'
                 '\n'
                 'Permission is hereby granted, free of charge, to any person \nobtaining a copy\n'
                 'of this software and associated documentation files \n(the "Software"), to deal\n'
                 'in the Software without restriction, including \nwithout limitation the rights\n'
                 'to use, copy, modify, merge, publish, distribute, \nsublicense, and/or sell\n'
                 'copies of the Software, and to permit persons to whom\n the Software is\n'
                 'furnished to do so, subject to the following conditions:\n'
                 '\n'
                 'The above copyright notice and this permission notice shall be included in all\n'
                 'copies or substantial portions of the Software.\n'
                 '\n'
                 'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY \nKIND, EXPRESS OR\n'
                 'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF \nMERCHANTABILITY,\n'
                 'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN \nNO EVENT SHALL THE\n'
                 'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, \nDAMAGES OR OTHER\n'
                 'LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR \nOTHERWISE, ARISING FROM,\n'
                 'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR \nOTHER DEALINGS IN THE\n'
                 'SOFTWARE.\n')

        Buttons.create('UsedLibs_GitHub_pypresence', 'SMALL', 'GitHub', UsedLibs.pypresence)

        add_separator()

        add_text('lxml')

        add_text('Copyright (c) 2004 Infrae. All rights reserved.\n'
                 '\n'
                 'Redistribution and use in source and binary forms, with or without\n'
                 'modification, are permitted provided that the following conditions are\n'
                 'met:\n'
                 '\n'
                 '  1. Redistributions of source code must retain the above copyright\n'
                 '     notice, this list of conditions and the following disclaimer.\n'
                 '   \n'
                 '  2. Redistributions in binary form must reproduce the above copyright\n'
                 '     notice, this list of conditions and the following disclaimer in\n'
                 '     the documentation and/or other materials provided with the\n'
                 '     distribution.\n'
                 '\n'
                 '  3. Neither the name of Infrae nor the names of its contributors may\n'
                 '     be used to endorse or promote products derived from this software\n'
                 '     without specific prior written permission.\n'
                 '\n'
                 'THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT \nHOLDERS AND CONTRIBUTORS\n'
                 '"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, \nINCLUDING, BUT NOT\n'
                 'LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY \nAND FITNESS FOR\n'
                 'A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT \nSHALL INFRAE OR\n'
                 'CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, \nINCIDENTAL, SPECIAL,\n'
                 'EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT \nNOT LIMITED TO,\n'
                 'PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF \nUSE, DATA, OR\n'
                 'PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED \nAND ON ANY THEORY OF\n'
                 'LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR \nTORT (INCLUDING\n'
                 'NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF \nTHE USE OF THIS\n'
                 'SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.')

        Buttons.create('UsedLibs_GitHub_lxml', 'SMALL', 'GitHub', UsedLibs.lxml)

        add_separator()

        add_text('requests')

        add_text('\n'
                 '                                                  Apache License\n'
                 '                                            Version 2.0, January 2004\n'
                 '                                       http://www.apache.org/licenses/\n'
                 '\n'
                 '   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND \n   DISTRIBUTION\n'
                 '\n'
                 '   1. Definitions.\n'
                 '\n'
                 '      "License" shall mean the terms and conditions for use, reproduction,\n'
                 '      and distribution as defined by Sections 1 through 9 of this document.\n'
                 '\n'
                 '      "Licensor" shall mean the copyright owner or entity authorized by\n'
                 '      the copyright owner that is granting the License.\n'
                 '\n'
                 '      "Legal Entity" shall mean the union of the acting entity and all\n'
                 '      other entities that control, are controlled by, or are under common\n'
                 '      control with that entity. For the purposes of this definition,\n'
                 '      "control" means (i) the power, direct or indirect, to cause the\n'
                 '      direction or management of such entity, whether by contract or\n'
                 '      otherwise, or (ii) ownership of fifty percent (50%) or more of the\n'
                 '      outstanding shares, or (iii) beneficial ownership of such entity.\n'
                 '\n'
                 '      "You" (or "Your") shall mean an individual or Legal Entity\n'
                 '      exercising permissions granted by this License.\n'
                 '\n'
                 '      "Source" form shall mean the preferred form for making modifications,\n'
                 '      including but not limited to software source code, documentation\n'
                 '      source, and configuration files.\n'
                 '\n'
                 '      "Object" form shall mean any form resulting from mechanical\n'
                 '      transformation or translation of a Source form, including but\n'
                 '      not limited to compiled object code, generated documentation,\n'
                 '      and conversions to other media types.\n'
                 '\n'
                 '      "Work" shall mean the work of authorship, whether in Source or\n'
                 '      Object form, made available under the License, as indicated by a\n'
                 '      copyright notice that is included in or attached to the work\n'
                 '      (an example is provided in the Appendix below).\n'
                 '\n'
                 '      "Derivative Works" shall mean any work, whether in Source or Object\n'
                 '      form, that is based on (or derived from) the Work and for which the\n'
                 '      editorial revisions, annotations, elaborations, or other modifications\n'
                 '      represent, as a whole, an original work of authorship. For the purposes\n'
                 '      of this License, Derivative Works shall not include works that remain\n'
                 '      separable from, or merely link (or bind by name) to the interfaces of,\n'
                 '      the Work and Derivative Works thereof.\n'
                 '\n'
                 '      "Contribution" shall mean any work of authorship, including\n'
                 '      the original version of the Work and any modifications or additions\n'
                 '      to that Work or Derivative Works thereof, that is intentionally\n'
                 '      submitted to Licensor for inclusion in the Work by the copyright owner\n'
                 '      or by an individual or Legal Entity authorized to submit on behalf of\n'
                 '      the copyright owner. For the purposes of this definition, "submitted"\n'
                 '      means any form of electronic, verbal, or written communication sent\n'
                 '      to the Licensor or its representatives, including but not limited to\n'
                 '      communication on electronic mailing lists, source code control systems,\n'
                 '      and issue tracking systems that are managed by, or on behalf of, the\n'
                 '      Licensor for the purpose of discussing and improving the Work, but\n'
                 '      excluding communication that is conspicuously marked or otherwise\n'
                 '      designated in writing by the copyright owner as "Not a Contribution."\n'
                 '\n'
                 '      "Contributor" shall mean Licensor and any individual or Legal Entity\n'
                 '      on behalf of whom a Contribution has been received by Licensor and\n'
                 '      subsequently incorporated within the Work.\n'
                 '\n'
                 '   2. Grant of Copyright License. Subject to the terms and conditions of\n'
                 '      this License, each Contributor hereby grants to You a perpetual,\n'
                 '      worldwide, non-exclusive, no-charge, royalty-free, irrevocable\n'
                 '      copyright license to reproduce, prepare Derivative Works of,\n'
                 '      publicly display, publicly perform, sublicense, and distribute the\n'
                 '      Work and such Derivative Works in Source or Object form.\n'
                 '\n'
                 '   3. Grant of Patent License. Subject to the terms and conditions of\n'
                 '      this License, each Contributor hereby grants to You a perpetual,\n'
                 '      worldwide, non-exclusive, no-charge, royalty-free, irrevocable\n'
                 '      (except as stated in this section) patent license to make, have made,\n'
                 '      use, offer to sell, sell, import, and otherwise transfer the Work,\n'
                 '      where such license applies only to those patent claims licensable\n'
                 '      by such Contributor that are necessarily infringed by their\n'
                 '      Contribution(s) alone or by combination of their Contribution(s)\n'
                 '      with the Work to which such Contribution(s) was submitted. If You\n'
                 '      institute patent litigation against any entity (including a\n'
                 '      cross-claim or counterclaim in a lawsuit) alleging that the Work\n'
                 '      or a Contribution incorporated within the Work constitutes direct\n'
                 '      or contributory patent infringement, then any patent licenses\n'
                 '      granted to You under this License for that Work shall terminate\n'
                 '      as of the date such litigation is filed.\n'
                 '\n'
                 '   4. Redistribution. You may reproduce and distribute copies of the\n'
                 '      Work or Derivative Works thereof in any medium, with or without\n'
                 '      modifications, and in Source or Object form, provided that You\n'
                 '      meet the following conditions:\n'
                 '\n'
                 '      (a) You must give any other recipients of the Work or\n'
                 '          Derivative Works a copy of this License; and\n'
                 '\n'
                 '      (b) You must cause any modified files to carry prominent notices\n'
                 '          stating that You changed the files; and\n'
                 '\n'
                 '      (c) You must retain, in the Source form of any Derivative Works\n'
                 '          that You distribute, all copyright, patent, trademark, and\n'
                 '          attribution notices from the Source form of the Work,\n'
                 '          excluding those notices that do not pertain to any part of\n'
                 '          the Derivative Works; and\n'
                 '\n'
                 '      (d) If the Work includes a "NOTICE" text file as part of its\n'
                 '          distribution, then any Derivative Works that You distribute must\n'
                 '          include a readable copy of the attribution notices contained\n'
                 '          within such NOTICE file, excluding those notices that do not\n'
                 '          pertain to any part of the Derivative Works, in at least one\n'
                 '          of the following places: within a NOTICE text file distributed\n'
                 '          as part of the Derivative Works; within the Source form or\n'
                 '          documentation, if provided along with the Derivative Works; or,\n'
                 '          within a display generated by the Derivative Works, if and\n'
                 '          wherever such third-party notices normally appear. The contents\n'
                 '          of the NOTICE file are for informational purposes only and\n'
                 '          do not modify the License. You may add Your own attribution\n'
                 '          notices within Derivative Works that You distribute, alongside\n'
                 '          or as an addendum to the NOTICE text from the Work, provided\n'
                 '          that such additional attribution notices cannot be construed\n'
                 '          as modifying the License.\n'
                 '\n'
                 '      You may add Your own copyright statement to Your modifications and\n'
                 '      may provide additional or different license terms and conditions\n'
                 '      for use, reproduction, or distribution of Your modifications, or\n'
                 '      for any such Derivative Works as a whole, provided Your use,\n'
                 '      reproduction, and distribution of the Work otherwise complies with\n'
                 '      the conditions stated in this License.\n'
                 '\n'
                 '   5. Submission of Contributions. Unless You explicitly state otherwise,\n'
                 '      any Contribution intentionally submitted for inclusion in the Work\n'
                 '      by You to the Licensor shall be under the terms and conditions of\n'
                 '      this License, without any additional terms or conditions.\n'
                 '      Notwithstanding the above, nothing herein shall supersede or modify\n'
                 '      the terms of any separate license agreement you may have executed\n'
                 '      with Licensor regarding such Contributions.\n'
                 '\n'
                 '   6. Trademarks. This License does not grant permission to use the trade\n'
                 '      names, trademarks, service marks, or product names of the Licensor,\n'
                 '      except as required for reasonable and customary use in describing the\n'
                 '      origin of the Work and reproducing the content of the NOTICE file.\n'
                 '\n'
                 '   7. Disclaimer of Warranty. Unless required by applicable law or\n'
                 '      agreed to in writing, Licensor provides the Work (and each\n'
                 '      Contributor provides its Contributions) on an "AS IS" BASIS,\n'
                 '      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either \n      express or\n'
                 '      implied, including, without limitation, any warranties or conditions\n'
                 '      of TITLE, NON-INFRINGEMENT, \nMERCHANTABILITY, or FITNESS FOR A\n'
                 '      PARTICULAR PURPOSE. You are solely responsible \nfor determining the'
                 '      appropriateness of using or redistributing the Work \nand assume any'
                 '      risks associated with Your exercise of permissions under this License.\n'
                 '\n'
                 '   8. Limitation of Liability. In no event and under no legal theory,\n'
                 '      whether in tort (including negligence), contract, or otherwise,\n'
                 '      unless required by applicable law (such as deliberate and grossly\n'
                 '      negligent acts) or agreed to in writing, shall any Contributor be\n'
                 '      liable to You for damages, including any direct, indirect, special,\n'
                 '      incidental, or consequential damages of any character arising as a\n'
                 '      result of this License or out of the use or inability to use the\n'
                 '      Work (including but not limited to damages for loss of goodwill,\n'
                 '      work stoppage, computer failure or malfunction, or any and all\n'
                 '      other commercial damages or losses), even if such Contributor\n'
                 '      has been advised of the possibility of such damages.\n'
                 '\n'
                 '   9. Accepting Warranty or Additional Liability. While redistributing\n'
                 '      the Work or Derivative Works thereof, You may choose to offer,\n'
                 '      and charge a fee for, acceptance of support, warranty, indemnity,\n'
                 '      or other liability obligations and/or rights consistent with this\n'
                 '      License. However, in accepting such obligations, You may act only\n'
                 '      on Your own behalf and on Your sole responsibility, not on behalf\n'
                 '      of any other Contributor, and only if You agree to indemnify,\n'
                 '      defend, and hold each Contributor harmless for any liability\n'
                 '      incurred by, or claims asserted against, such Contributor by reason\n'
                 '      of your accepting any such warranty or additional liability.\n')

        Buttons.create('UsedLibs_GitHub_requests', 'SMALL', 'GitHub', UsedLibs.requests)

        add_separator()

        add_text('Pillow')

        add_text('The Python Imaging Library (PIL) is\n'
                 '\n'
                 '    Copyright © 1997-2011 by Secret Labs AB\n'
                 '    Copyright © 1995-2011 by Fredrik Lundh\n'
                 '\n'
                 'Pillow is the friendly PIL fork. It is\n'
                 '\n'
                 '    Copyright © 2010-2021 by Alex Clark and contributors\n'
                 '\n'
                 'Like PIL, Pillow is licensed under the open source HPND License:\n'
                 '\n'
                 'By obtaining, using, and/or copying this software and/or its associated\n'
                 'documentation, you agree that you have read, understood, and will comply\n'
                 'with the following terms and conditions:\n'
                 '\n'
                 'Permission to use, copy, modify, and distribute \nthis software and its\n'
                 'associated documentation for any purpose and \nwithout fee is hereby granted,\n'
                 'provided that the above copyright notice appears \nin all copies, and that\n'
                 'both that copyright notice and this permission notice \nappear in supporting\n'
                 'documentation, and that the name of Secret Labs AB \nor the author not be\n'
                 'used in advertising or publicity pertaining to \ndistribution of the software\n'
                 'without specific, written prior permission.\n'
                 '\n'
                 'SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES \nWITH REGARD TO THIS\n'
                 'SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF \nMERCHANTABILITY AND FITNESS.\n'
                 'IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE \nFOR ANY SPECIAL,\n'
                 'INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES \nWHATSOEVER RESULTING FROM\n'
                 'LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF \nCONTRACT, NEGLIGENCE\n'
                 'OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION \nWITH THE USE OR\n'
                 'PERFORMANCE OF THIS SOFTWARE.\n')

        Buttons.create('UsedLibs_GitHub_pillow', 'SMALL', 'GitHub', UsedLibs.pillow)

        add_separator()

        add_text('pywin32')

        add_text('PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2\n'
                 '\n'
                 '1. This LICENSE AGREEMENT is between the Python \nSoftware Foundation ("PSF"), and the Individual or Organization \n'
                 '("Licensee") accessing and otherwise using this software\n ("Python") in source or binary form and its associated documentation.\n'
                 '2. Subject to the terms and conditions of this License \nAgreement, PSF hereby grants Licensee a nonexclusive, royalty-free, \n'
                 'world-wide license to reproduce, analyze, test, perform \nand/or display publicly, prepare derivative works, distribute, and \n'
                 "otherwise use Python alone or in any derivative \nversion, provided, however, that PSF's License Agreement and \n"
                 "PSF's notice of copyright, i.e., \n" +
                 '"Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006 \nPython Software Foundation; All Rights Reserved\n' +
                 "are retained in Python alone or in any derivative version \nprepared by Licensee.\n"
                 '3. In the event Licensee prepares a derivative work that is \nbased on or incorporates Python or any part thereof, and wants \n'
                 'to make the derivative work available to others as provided \nherein, then Licensee hereby agrees to include in any such work \n'
                 'a brief summary of the changes made to Python.\n'
                 '4. PSF is making Python available to Licensee on \nan "AS IS" basis. PSF MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR \n'
                 'IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, \nPSF MAKES NO AND DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY \n'
                 'OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE \nOF PYTHON WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.'
                 '5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS \nOF PYTHON FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR \n'
                 'LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR \nOTHERWISE USING PYTHON, OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF THE \n'
                 'POSSIBILITY THEREOF.\n'
                 '6. This License Agreement will automatically terminate \nupon a material breach of its terms and conditions.\n'
                 '7. Nothing in this License Agreement shall be deemed to \ncreate any relationship of agency, partnership, or joint venture \n'
                 'between PSF and Licensee. This License Agreement does not \ngrant permission to use PSF trademarks or trade name in a trademark \n'
                 'sense to endorse or promote products or services of \nLicensee, or any third party.'
                 '8. By copying, installing or otherwise using Python, \nLicensee agrees to be bound by the terms and conditions of this License Agreement.')

        Buttons.create('UsedLibs_GitHub_pywin32', 'SMALL', 'GitHub', UsedLibs.pywin32)

        add_separator()
        Buttons.create('LibsCloseButton', 'LARGE', 'Close', UsedLibs.close_libs)
