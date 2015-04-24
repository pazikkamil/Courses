pollutantmean <- function(directory, pollutant, id = 1:332) {
  
  setwd(directory)
  l_files <- dir()
  Data <- lapply(l_files[id], read.csv)
  df_data  <- do.call("rbind",Data)
  i_value <- mean(df_data[,pollutant], na.rm = TRUE)
  return (i_value)
}