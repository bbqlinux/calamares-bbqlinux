/* === This file is part of Calamares - <http://github.com/calamares> ===
 *
 *   Copyright 2015, Teo Mrnjavac <teo@kde.org>
 *
 *   Calamares is free software: you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation, either version 3 of the License, or
 *   (at your option) any later version.
 *
 *   Calamares is distributed in the hope that it will be useful,
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 *   GNU General Public License for more details.
 *
 *   You should have received a copy of the GNU General Public License
 *   along with Calamares. If not, see <http://www.gnu.org/licenses/>.
 */

import QtQuick 2.0;
import calamares.slideshow 1.0;

Presentation
{
    id: presentation

    Timer {
        interval: 5000
        running: false
        repeat: true
        onTriggered: presentation.goToNextSlide()
    }
    
    Slide {
        Image {
            id: slide1
            source: "slide_1.jpg"
            width: 586; height: 344
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
    }

    Slide {
        Image {
            id: slide2
            source: "slide_2.jpg"
            width: 586; height: 344
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
    }

    Slide {
        Image {
            id: slide3
            source: "slide_3.jpg"
            width: 586; height: 344
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
    }

    Slide {
        Image {
            id: slide4
            source: "slide_4.jpg"
            width: 586; height: 344
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
    }
}
