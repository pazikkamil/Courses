# Finding and replacing

```bash
:%s/=/:/gc #from/to/global/confirm
:s/;/\n/gc # just for one line 
```

# settings
syntax on
set number # rownumber
set no number
set hlsearch # podswietla wyszukiwanie nohl
set incsearch
set autoindent

## Tabs

- tabe (open tab)
- v-g-t / g-T (next tabl / previous)

## Filetypes
- set filetype=python

## Launch
- !make
- !wc -l % # show lines of current file

## Mappings
- :map <F5> :! wc -l %<CR> 
- :imap amk ala ma kota #=amk

## Code completation
- ctrl + n
