## 'directory' is a character vector of length 1 indicating
## the location of the CSV files

## 'id' is an integer vector indicating the monitor ID numbers
## to be used

## Return a data frame of the form:
## id nobs
## 1  117
## 2  1041
## ...
## where 'id' is the monitor ID number and 'nobs' is the
## nrow(subset(df_data,is.na(nitrate) == FALSE & is.na(sulfate) == FALSE & ID == 2 ,  select = c("ID")))

complete <- function(directory, id = 1:332) {
  setwd(directory)
  l_files <- dir()
  n_count <- length(id)
  n_start <- id[1]
  Data <- lapply(l_files[id], read.csv)
  df_data  <- do.call("rbind",Data)
  v_1 <- vector(length = n_count)
  v_2 <- vector(length = n_count)
  
  for (i in 1:n_count)
  {
    v_1[i] <- n_start
    v_2[i] <- nrow(subset(df_data,is.na(nitrate) == FALSE & is.na(sulfate) == FALSE & ID == n_start ,  select = c("ID")))
    n_start <- n_start + 1
  }
  return (data.frame(v_1 , v_2))
}
  