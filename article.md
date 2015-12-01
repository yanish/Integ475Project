---
title: "Mini_project_3 Wetlands data analysis"
output: html_document
---

This is an R Markdown document. Markdown is a simple formatting syntax for authoring HTML, PDF, and MS Word documents. For more details on using R Markdown see <http://rmarkdown.rstudio.com>.

When you click the **Knit** button a document will be generated that includes both content as well as the output of any embedded R code chunks within the document. You can embed an R code chunk like this:



```r
library(igraph)
library(dplyr)
library(networkD3)
library(network)
library(ggplot2)
setwd("/Users/Yanish/Documents/Fall_2015/Integ_475/mini_project_2/Integ475Project")

network <- read.graph("networks/net.graphml", format = "graphml" )
data_wetlands <- read.csv("data/dat.csv")

data <- select(data_wetlands, AF, SO, DT, PU, PI, PY, WC, SC, CL, SP, numAuthors)

glimpse(data)
```

```
## Observations: 1,739
## Variables: 11
## $ AF         (fctr) Crigger, DK|Graves, GA|Fike, DL, Drouin, Ariane|Sa...
## $ SO         (fctr) WETLANDS, WETLANDS, ENVIRONMENTAL POLLUTION, WETLA...
## $ DT         (fctr) Article, Article, Article, Article, Article, Artic...
## $ PU         (fctr) SOC WETLAND SCIENTISTS, SPRINGER, ELSEVIER SCI LTD...
## $ PI         (fctr) LAWRENCE, DORDRECHT, OXFORD, DORDRECHT, DORDRECHT,...
## $ PY         (int) 2005, 2011, 2003, 1996, 2007, 2006, 2009, 2002, 201...
## $ WC         (fctr) Ecology; Environmental Sciences, Ecology; Environm...
## $ SC         (fctr) Environmental Sciences & Ecology, Environmental Sc...
## $ CL         (fctr) , , , , , , , , , , , , , , , , , , , , , , , , 
## $ SP         (fctr) , , , , , , , , , , , , , , , , , , , , , , , , 
## $ numAuthors (fctr) 3, 4, 4, 4, 4, 4, 1, 4, 6, 7, 4, 3, 2, 2, 2, 1, 4,...
```

```r
glimpse(data_wetlands)
```

```
## Observations: 1,739
## Variables: 54
## $ UT         (fctr) WOS:000234192800012, WOS:000297864900014, WOS:0001...
## $ PT         (fctr) J, J, J, J, J, J, J, J, J, J, J, J, J, J, J, J, J,...
## $ TI         (fctr) Lake Worth Lagoon conceptual ecological model, Hig...
## $ AF         (fctr) Crigger, DK|Graves, GA|Fike, DL, Drouin, Ariane|Sa...
## $ CR         (fctr) McCook LJ, 2001, CORAL REEFS, V19, P400|Valiela I,...
## $ AU         (fctr) Crigger, DK|Graves, GA|Fike, DL, Drouin, A|Saint-L...
## $ SO         (fctr) WETLANDS, WETLANDS, ENVIRONMENTAL POLLUTION, WETLA...
## $ LA         (fctr) English, English, English, English, English, Engli...
## $ DT         (fctr) Article, Article, Article, Article, Article, Artic...
## $ DE         (fctr) conceptual ecological model; Lake Worth Lagoon; sa...
## $ ID         (fctr) MACROALGAL BLOOMS; CORAL-REEFS; FLORIDA, SEDIMENTA...
## $ AB         (fctr) The Lake Worth Lagoon is a major estuarine water b...
## $ C1         (fctr) Florida Dept Environm Protect, W Palm Beach, FL 33...
## $ RP         (fctr) Crigger, DK (reprint author), Florida Dept Environ...
## $ EM         (fctr) Dianne.Crigger@dep.state.fl.us, diane.saint-lauren...
## $ NR         (int) 47, 42, 24, 65, 59, 49, 40, 33, 39, 27, 59, 56, 0, ...
## $ TC         (int) 2, 6, 3, 21, 4, 82, 11, 10, 1, 22, 7, 3, 63, 22, 31...
## $ Z9         (int) 4, 6, 3, 22, 4, 88, 11, 11, 1, 27, 10, 4, 64, 25, 3...
## $ U1         (int) 4, 4, 0, 3, 2, 4, 2, 1, 7, 4, 3, 8, 3, 5, 0, 4, 1, ...
## $ U2         (int) 8, 15, 2, 15, 4, 34, 21, 3, 32, 32, 24, 29, 6, 19, ...
## $ PU         (fctr) SOC WETLAND SCIENTISTS, SPRINGER, ELSEVIER SCI LTD...
## $ PI         (fctr) LAWRENCE, DORDRECHT, OXFORD, DORDRECHT, DORDRECHT,...
## $ PA         (fctr) 810 E TENTH ST, P O BOX 1897, LAWRENCE, KS 66044 U...
## $ SN         (fctr) 0277-5212, 0277-5212, 0269-7491, 0277-5212, 0277-5...
## $ J9         (fctr) WETLANDS, WETLANDS, ENVIRON POLLUT, WETLANDS, WETL...
## $ JI         (fctr) Wetlands, Wetlands, Environ. Pollut., Wetlands, We...
## $ PD         (fctr) DEC, DEC, , JUN, DEC, MAR, MAR, SEP, FEB, DEC, APR...
## $ PY         (int) 2005, 2011, 2003, 1996, 2007, 2006, 2009, 2002, 201...
## $ VL         (int) 25, 31, 125, 16, 27, 140, 29, 22, 35, 150, 30, 31, ...
## $ IS         (fctr) 4, 6, 3, 2, 4, 1, 1, 3, 1, 3, 2, 4, 3, 2, 3, 1, 1,...
## $ BP         (fctr) 943, 1151, 447, 134, 873, 136, 54, 541, 105, 313, ...
## $ EP         (fctr) 954, 1164, 451, 142, 883, 149, 65, 549, 113, 320, ...
## $ DI         (fctr) 10.1672/0277-5212(2005)025[0943:LWLCEM]2.0.CO;2, 1...
## $ PG         (int) 12, 14, 5, 9, 11, 14, 12, 9, 9, 8, 11, 12, 12, 18, ...
## $ WC         (fctr) Ecology; Environmental Sciences, Ecology; Environm...
## $ SC         (fctr) Environmental Sciences & Ecology, Environmental Sc...
## $ GA         (fctr) 996RT, 859GM, 705DA, UU259, 238TV, 007GK, 434SN, 6...
## $ FU         (fctr) , Natural Sciences and Engineering Research Counci...
## $ FX         (fctr) , We thank Natural Sciences and Engineering Resear...
## $ PM         (int) NA, NA, 12826422, NA, NA, 16112310, NA, NA, NA, 173...
## $ EI         (fctr) , , , 1943-6246, , , , , 1943-6246, , , 1943-6246,...
## $ RI         (fctr) , , , , , Covaci, Adrian/A-9058-2008, , , Johns, C...
## $ OI         (fctr) , , , , , Covaci, Adrian/0000-0003-0527-1136, , , ...
## $ BE         (fctr) , , , , , , , , , , , , , , , , , , , , , , , , 
## $ CT         (fctr) , , , , , , , , , , , , , , , , , , , , , , , , 
## $ CY         (fctr) , , , , , , , , , , , , , , , , , , , , , , , , 
## $ CL         (fctr) , , , , , , , , , , , , , , , , , , , , , , , , 
## $ SP         (fctr) , , , , , , , , , , , , , , , , , , , , , , , , 
## $ HO         (fctr) , , , , , , , , , , , , , , , , , , , , , , , , 
## $ BN         (fctr) , , , , , , , , , , , , , , , , , , , , , , , , 
## $ SI         (fctr) , , , , , , , , , , , , , , , , , , , , , , , , 
## $ AR         (fctr) , , , , , , , , , , , , , , , , , , , , , , , , 
## $ SU         (int) NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,...
## $ numAuthors (fctr) 3, 4, 4, 4, 4, 4, 1, 4, 6, 7, 4, 3, 2, 2, 2, 1, 4,...
```

```r
View(data_wetlands)

plot (network)
```

![plot of chunk unnamed-chunk-1](figure/unnamed-chunk-1-1.pdf) 
##Some text here just to make it seem like there will be text


You can also embed plots, for example:



Note that the `echo = FALSE` parameter was added to the code chunk to prevent printing of the R code that generated the plot.