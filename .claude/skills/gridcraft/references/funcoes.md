# Funções de planilha do GridCraft

Gerado por `gridcraft-cli functions`.

```
ABS(number)
    MathTrig: Absolute value of a number.
ACCRINT(issue, first_interest, settlement, rate, par, frequency, [basis], [calc_method])
    Financial: Accrued interest of a security paying periodic interest.
ACCRINTM(issue, settlement, rate, [par], [basis])
    Financial: Accrued interest of a security paying interest at maturity.
ACOS(number)
    MathTrig: Arccosine in radians.
ACOSH(number)
    MathTrig: Inverse hyperbolic cosine.
ACOT(number)
    MathTrig: Arccotangent in radians (0 to pi).
ACOTH(number)
    MathTrig: Inverse hyperbolic cotangent.
ADDRESS(row_num, column_num, [abs_num], [a1], [sheet_text])
    Lookup: Builds a cell address as text from row and column numbers.
AGGREGATE(function_num, options, ref1, ...)
    MathTrig: An aggregate that can skip hidden rows and errors.
AMORDEGRC(cost, date_purchased, first_period, salvage, period, rate, [basis])
    Financial: French degressive depreciation with a life-based coefficient.
AMORLINC(cost, date_purchased, first_period, salvage, period, rate, [basis])
    Financial: French linear depreciation prorated for the first period.
AND(logical1, [logical2], ...)
    Logical: TRUE when every argument is TRUE.
ARABIC(text)
    MathTrig: Converts Roman numerals to a number.
AREAS(reference)
    Lookup: Number of areas in a reference.
ARRAYTOTEXT(array, [format])
    Text: Converts an array to text, either as a comma list or as a strict array constant.
ASC(text)
    Text: Converts full-width characters to half-width (no change for single-byte text).
ASIN(number)
    MathTrig: Arcsine in radians.
ASINH(number)
    MathTrig: Inverse hyperbolic sine.
ATAN(number)
    MathTrig: Arctangent in radians.
ATAN2(x_num, y_num)
    MathTrig: Angle of the point (x, y) from the x-axis in radians.
ATANH(number)
    MathTrig: Inverse hyperbolic tangent.
AVEDEV(number1, [number2], ...)
    Statistical: Average absolute deviation from the mean.
AVERAGE(number1, [number2], ...)
    Statistical: Arithmetic mean of the numbers.
AVERAGEA(value1, [value2], ...)
    Statistical: Mean counting text as 0 and logical values as 1 or 0.
AVERAGEIF(range, criteria, [average_range])
    Statistical: Average of the cells that meet a condition.
AVERAGEIFS(average_range, criteria_range1, criteria1, ...)
    Statistical: Average of the cells that meet every condition.
BAHTTEXT(number)
    Text: Spells out a number in Thai words with Baht.
BASE(number, radix, [min_length])
    MathTrig: Writes a number in another base, padded with zeros.
BESSELI(x, n)
    Engineering: Modified Bessel function of the first kind, I_n(x).
BESSELJ(x, n)
    Engineering: Bessel function of the first kind, J_n(x).
BESSELK(x, n)
    Engineering: Modified Bessel function of the second kind, K_n(x).
BESSELY(x, n)
    Engineering: Bessel function of the second kind, Y_n(x).
BETA.DIST(x, alpha, beta, cumulative, [A], [B])
    Statistical: Beta distribution density or probability.
BETA.INV(probability, alpha, beta, [A], [B])
    Statistical: Inverse of the cumulative beta distribution.
BETADIST(x, alpha, beta, [A], [B])
    Compatibility: Cumulative beta probability.
BETAINV(probability, alpha, beta, [A], [B])
    Compatibility: Inverse of the cumulative beta distribution.
BIN2DEC(number)
    Engineering: Converts a binary number to decimal.
BIN2HEX(number, [places])
    Engineering: Converts a binary number to hexadecimal.
BIN2OCT(number, [places])
    Engineering: Converts a binary number to octal.
BINOM.DIST(number_s, trials, probability_s, cumulative)
    Statistical: Binomial probability.
BINOM.DIST.RANGE(trials, probability_s, number_s, [number_s2])
    Statistical: Probability of a number of successes falling in a range.
BINOM.INV(trials, probability_s, alpha)
    Statistical: Smallest success count whose cumulative binomial probability reaches alpha.
BINOMDIST(number_s, trials, probability_s, cumulative)
    Compatibility: Binomial probability.
BITAND(number1, number2)
    Engineering: Bitwise AND of two non-negative integers.
BITLSHIFT(number, shift_amount)
    Engineering: Shifts the bits of a number left (right for negative shifts).
BITOR(number1, number2)
    Engineering: Bitwise OR of two non-negative integers.
BITRSHIFT(number, shift_amount)
    Engineering: Shifts the bits of a number right (left for negative shifts).
BITXOR(number1, number2)
    Engineering: Bitwise exclusive OR of two non-negative integers.
BYCOL(array, lambda)
    Logical: Applies a LAMBDA to each column.
BYROW(array, lambda)
    Logical: Applies a LAMBDA to each row.
CEILING(number, significance)
    Compatibility: Rounds a number up to a multiple of significance.
CEILING.MATH(number, [significance], [mode])
    MathTrig: Rounds a number up to the nearest integer or multiple.
CEILING.PRECISE(number, [significance])
    MathTrig: Rounds a number toward positive infinity to a multiple.
CELL(info_type, [reference])
    Information: Information about a cell.
CHAR(number)
    Text: Returns the character for a code from the Windows-1252 character set.
CHIDIST(x, deg_freedom)
    Compatibility: Right-tailed chi-squared probability.
CHIINV(probability, deg_freedom)
    Compatibility: Inverse of the right-tailed chi-squared distribution.
CHISQ.DIST(x, deg_freedom, cumulative)
    Statistical: Chi-squared density or left-tailed probability.
CHISQ.DIST.RT(x, deg_freedom)
    Statistical: Right-tailed chi-squared probability.
CHISQ.INV(probability, deg_freedom)
    Statistical: Inverse of the left-tailed chi-squared distribution.
CHISQ.INV.RT(probability, deg_freedom)
    Statistical: Inverse of the right-tailed chi-squared distribution.
CHISQ.TEST(actual_range, expected_range)
    Statistical: Chi-squared test of independence.
CHITEST(actual_range, expected_range)
    Compatibility: Chi-squared test of independence.
CHOOSE(index_num, value1, [value2], ...)
    Lookup: Picks a value from the list by its position.
CHOOSECOLS(array, col_num1, [col_num2], ...)
    Lookup: Picks columns of an array by position (negative counts from the end).
CHOOSEROWS(array, row_num1, [row_num2], ...)
    Lookup: Picks rows of an array by position (negative counts from the end).
CLEAN(text)
    Text: Removes non-printable control characters from text.
CODE(text)
    Text: Returns the Windows-1252 code of the first character of a text.
COLUMN([reference])
    Lookup: Column number of a reference.
COLUMNS(array)
    Lookup: Counts the columns in an array or range.
COMBIN(number, number_chosen)
    MathTrig: Number of combinations without repetition.
COMBINA(number, number_chosen)
    MathTrig: Number of combinations with repetition.
COMPLEX(real_num, i_num, [suffix])
    Engineering: Builds a complex number as text from real and imaginary parts.
CONCAT(text1, [text2], ...)
    Text: Joins text from values and every cell of ranges, without a separator.
CONCATENATE(text1, [text2], ...)
    Text: Joins several text values into one.
CONFIDENCE(alpha, standard_dev, size)
    Compatibility: Confidence interval half-width using the normal distribution.
CONFIDENCE.NORM(alpha, standard_dev, size)
    Statistical: Confidence interval half-width using the normal distribution.
CONFIDENCE.T(alpha, standard_dev, size)
    Statistical: Confidence interval half-width using Student's t distribution.
CONVERT(number, from_unit, to_unit)
    Engineering: Converts a measurement from one unit to another.
CORREL(array1, array2)
    Statistical: Correlation coefficient of two data sets.
COS(number)
    MathTrig: Cosine of an angle in radians.
COSH(number)
    MathTrig: Hyperbolic cosine.
COT(number)
    MathTrig: Cotangent of an angle in radians.
COTH(number)
    MathTrig: Hyperbolic cotangent.
COUNT(value1, [value2], ...)
    Statistical: Counts the numbers.
COUNTA(value1, [value2], ...)
    Statistical: Counts the non-empty values.
COUNTBLANK(range)
    Statistical: Counts empty cells and empty text in a range.
COUNTIF(range, criteria)
    Statistical: Counts the cells that meet a condition.
COUNTIFS(criteria_range1, criteria1, ...)
    Statistical: Counts the cells that meet every condition.
COUPDAYBS(settlement, maturity, frequency, [basis])
    Financial: Days from the start of the coupon period to settlement.
COUPDAYS(settlement, maturity, frequency, [basis])
    Financial: Days in the coupon period that contains settlement.
COUPDAYSNC(settlement, maturity, frequency, [basis])
    Financial: Days from settlement to the next coupon date.
COUPNCD(settlement, maturity, frequency, [basis])
    Financial: Next coupon date after settlement.
COUPNUM(settlement, maturity, frequency, [basis])
    Financial: Number of coupons payable between settlement and maturity.
COUPPCD(settlement, maturity, frequency, [basis])
    Financial: Previous coupon date on or before settlement.
COVAR(array1, array2)
    Compatibility: Population covariance of paired values.
COVARIANCE.P(array1, array2)
    Statistical: Population covariance of paired values.
COVARIANCE.S(array1, array2)
    Statistical: Sample covariance of paired values.
CRITBINOM(trials, probability_s, alpha)
    Compatibility: Smallest success count whose cumulative binomial probability reaches alpha.
CSC(number)
    MathTrig: Cosecant of an angle in radians.
CSCH(number)
    MathTrig: Hyperbolic cosecant.
CUBEKPIMEMBER(connection, kpi_name, kpi_property, [caption])
    Cube: Returns a key performance indicator property from a cube (no cube connections; #N/A).
CUBEMEMBER(connection, member_expression, [caption])
    Cube: Returns a member or tuple from a cube (no cube connections; #N/A).
CUBEMEMBERPROPERTY(connection, member_expression, property)
    Cube: Returns a property of a cube member (no cube connections; #N/A).
CUBERANKEDMEMBER(connection, set_expression, rank, [caption])
    Cube: Returns the nth member of a cube set (no cube connections; #N/A).
CUBESET(connection, set_expression, [caption], [sort_order], [sort_by])
    Cube: Defines a set of cube members (no cube connections; #N/A).
CUBESETCOUNT(set)
    Cube: Counts the items in a cube set (no cube connections; #N/A).
CUBEVALUE(connection, [member_expression1], ...)
    Cube: Returns an aggregated value from a cube (no cube connections; #N/A).
CUMIPMT(rate, nper, pv, start_period, end_period, type)
    Financial: Total interest paid between two periods.
CUMPRINC(rate, nper, pv, start_period, end_period, type)
    Financial: Total principal repaid between two periods.
DATE(year, month, day)
    DateTime: Builds a date serial number from a year, month and day.
DATEDIF(start_date, end_date, unit)
    DateTime: Counts whole years, months or days between two dates. unit: Y, M, D, MD, YM or YD.
DATEVALUE(date_text)
    DateTime: Converts a date written as text into a date serial number.
DAVERAGE(database, field, criteria)
    Database: Averages the numbers in a field of the records that meet the criteria.
DAY(serial_number)
    DateTime: Returns the day of the month of a date.
DAYS(end_date, start_date)
    DateTime: Returns the number of days between two dates.
DAYS360(start_date, end_date, [method])
    DateTime: Counts days between two dates on a 360-day year (US or European method).
DB(cost, salvage, life, period, [month])
    Financial: Fixed-declining-balance depreciation for a period.
DBCS(text)
    Text: Converts half-width characters to full-width (no change in this locale).
DCOUNT(database, [field], criteria)
    Database: Counts numeric cells in a field of the matching records (or the matching records).
DCOUNTA(database, [field], criteria)
    Database: Counts non-blank cells in a field of the matching records (or the matching records).
DDB(cost, salvage, life, period, [factor])
    Financial: Double-declining-balance (or other factor) depreciation for a period.
DEC2BIN(number, [places])
    Engineering: Converts a decimal number to binary.
DEC2HEX(number, [places])
    Engineering: Converts a decimal number to hexadecimal.
DEC2OCT(number, [places])
    Engineering: Converts a decimal number to octal.
DECIMAL(text, radix)
    MathTrig: Reads text in a given base as a number.
DEGREES(angle)
    MathTrig: Converts radians to degrees.
DELTA(number1, [number2])
    Engineering: Returns 1 when two numbers are equal, otherwise 0.
DEVSQ(number1, [number2], ...)
    Statistical: Sum of squared deviations from the mean.
DGET(database, field, criteria)
    Database: Returns the field value of the single record that meets the criteria.
DISC(settlement, maturity, pr, redemption, [basis])
    Financial: Discount rate of a security.
DMAX(database, field, criteria)
    Database: Largest number in a field of the matching records.
DMIN(database, field, criteria)
    Database: Smallest number in a field of the matching records.
DOLLAR(number, [decimals])
    Text: Formats a number as currency text.
DOLLARDE(fractional_dollar, fraction)
    Financial: Converts a fractional price notation to a decimal number.
DOLLARFR(decimal_dollar, fraction)
    Financial: Converts a decimal price to fractional notation.
DPRODUCT(database, field, criteria)
    Database: Multiplies the numbers in a field of the matching records.
DROP(array, rows, [columns])
    Lookup: Removes rows or columns from the start (or end) of an array.
DSTDEV(database, field, criteria)
    Database: Sample standard deviation of a field over the matching records.
DSTDEVP(database, field, criteria)
    Database: Population standard deviation of a field over the matching records.
DSUM(database, field, criteria)
    Database: Adds the numbers in a field of the records that meet the criteria.
DURATION(settlement, maturity, coupon, yld, frequency, [basis])
    Financial: Macaulay duration of a security with periodic interest.
DVAR(database, field, criteria)
    Database: Sample variance of a field over the matching records.
DVARP(database, field, criteria)
    Database: Population variance of a field over the matching records.
EDATE(start_date, months)
    DateTime: Returns the date a number of months before or after a date.
EFFECT(nominal_rate, npery)
    Financial: Effective annual rate from a nominal rate and compounding periods.
ENCODEURL(text)
    Web: Percent-encodes text for use in a URL.
EOMONTH(start_date, months)
    DateTime: Returns the last day of the month a number of months away.
ERF(lower_limit, [upper_limit])
    Engineering: Error function integrated from 0 to a limit, or between two limits.
ERF.PRECISE(x)
    Engineering: Error function integrated from 0 to x.
ERFC(x)
    Engineering: Complementary error function, 1 - ERF(x).
ERFC.PRECISE(x)
    Engineering: Complementary error function, 1 - ERF(x).
ERROR.TYPE(error_val)
    Information: Returns the number identifying an error value, or #N/A if it is not an error.
EUROCONVERT(number, source, target, [full_precision], [triangulation_precision])
    AddIn: Converts between the euro and the former euro member currencies at the fixed rates.
EVEN(number)
    MathTrig: Rounds away from zero to the nearest even integer.
EXACT(text1, text2)
    Text: TRUE when two texts are identical, including case.
EXP(number)
    MathTrig: e raised to the given power.
EXPAND(array, rows, [columns], [pad_with])
    Lookup: Grows an array to the given size, filling new cells with a pad value.
EXPON.DIST(x, lambda, cumulative)
    Statistical: Exponential distribution density or probability.
EXPONDIST(x, lambda, cumulative)
    Compatibility: Exponential distribution density or probability.
F.DIST(x, deg_freedom1, deg_freedom2, cumulative)
    Statistical: F distribution density or left-tailed probability.
F.DIST.RT(x, deg_freedom1, deg_freedom2)
    Statistical: Right-tailed F probability.
F.INV(probability, deg_freedom1, deg_freedom2)
    Statistical: Inverse of the left-tailed F distribution.
F.INV.RT(probability, deg_freedom1, deg_freedom2)
    Statistical: Inverse of the right-tailed F distribution.
F.TEST(array1, array2)
    Statistical: Two-tailed probability that two variances do not differ.
FACT(number)
    MathTrig: Factorial of a number.
FACTDOUBLE(number)
    MathTrig: Double factorial of a number.
FALSE()
    Logical: Returns the logical value FALSE.
FDIST(x, deg_freedom1, deg_freedom2)
    Compatibility: Right-tailed F probability.
FILTER(array, include, [if_empty])
    Lookup: Keeps the rows or columns of an array whose include flag is TRUE.
FILTERXML(xml, xpath)
    Web: Extracts data from XML with an XPath (not available; returns #VALUE!).
FIND(find_text, within_text, [start_num])
    Text: Finds the position of one text in another (case-sensitive).
FINDB(find_text, within_text, [start_num])
    Text: Byte version of FIND.
FINV(probability, deg_freedom1, deg_freedom2)
    Compatibility: Inverse of the right-tailed F distribution.
FISHER(x)
    Statistical: Fisher transformation.
FISHERINV(y)
    Statistical: Inverse of the Fisher transformation.
FIXED(number, [decimals], [no_commas])
    Text: Rounds a number and formats it as text with fixed decimals and optional thousands separators.
FLOOR(number, significance)
    Compatibility: Rounds a number down to a multiple of significance.
FLOOR.MATH(number, [significance], [mode])
    MathTrig: Rounds a number down to the nearest integer or multiple.
FLOOR.PRECISE(number, [significance])
    MathTrig: Rounds a number toward negative infinity to a multiple.
FORECAST(x, known_ys, known_xs)
    Compatibility: Predicts a value along a linear trend.
FORECAST.ETS(target_date, values, timeline, [seasonality], [data_completion], [aggregation])
    Statistical: Forecasts a value by additive (AAA) exponential smoothing.
FORECAST.ETS.CONFINT(target_date, values, timeline, [confidence_level], [seasonality], [data_completion], [aggregation])
    Statistical: Half-width of the confidence interval around a FORECAST.ETS value.
FORECAST.ETS.SEASONALITY(values, timeline, [data_completion], [aggregation])
    Statistical: Length of the repeating pattern detected in a time series.
FORECAST.ETS.STAT(values, timeline, statistic_type, [seasonality], [data_completion], [aggregation])
    Statistical: A statistic of the FORECAST.ETS model: 1 alpha, 2 beta, 3 gamma, 4 MASE, 5 SMAPE, 6 MAE, 7 RMSE, 8 step size.
FORECAST.LINEAR(x, known_ys, known_xs)
    Statistical: Predicts a value along a linear trend.
FORMULATEXT(reference)
    Lookup: The formula of a cell as text.
FREQUENCY(data_array, bins_array)
    Statistical: Counts how many values fall into each bin, as a vertical array.
FTEST(array1, array2)
    Compatibility: Two-tailed probability that two variances do not differ.
FV(rate, nper, pmt, [pv], [type])
    Financial: Future value of an investment with constant payments and rate.
FVSCHEDULE(principal, schedule)
    Financial: Future value of a principal after a series of compound rates.
GAMMA(number)
    Statistical: The gamma function.
GAMMA.DIST(x, alpha, beta, cumulative)
    Statistical: Gamma distribution density or probability.
GAMMA.INV(probability, alpha, beta)
    Statistical: Inverse of the gamma cumulative distribution.
GAMMADIST(x, alpha, beta, cumulative)
    Compatibility: Gamma distribution density or probability.
GAMMAINV(probability, alpha, beta)
    Compatibility: Inverse of the gamma cumulative distribution.
GAMMALN(x)
    Statistical: Natural log of the gamma function.
GAMMALN.PRECISE(x)
    Statistical: Natural log of the gamma function.
GAUSS(z)
    Statistical: Probability that a standard normal value falls between the mean and z.
GCD(number1, [number2], ...)
    MathTrig: Greatest common divisor of integers.
GEOMEAN(number1, [number2], ...)
    Statistical: Geometric mean of positive numbers.
GESTEP(number, [step])
    Engineering: Returns 1 when a number is at least the step, otherwise 0.
GROUPBY(row_fields, values, function, [field_headers], [total_depth], [sort_order], [filter_array], [field_relationship])
    Lookup: Groups rows by key fields and aggregates the values of each group.
GROWTH(known_ys, [known_xs], [new_xs], [const])
    Statistical: Values along a fitted exponential growth curve.
HARMEAN(number1, [number2], ...)
    Statistical: Harmonic mean of positive numbers.
HEX2BIN(number, [places])
    Engineering: Converts a hexadecimal number to binary.
HEX2DEC(number)
    Engineering: Converts a hexadecimal number to decimal.
HEX2OCT(number, [places])
    Engineering: Converts a hexadecimal number to octal.
HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])
    Lookup: Finds a value in the first row of a table and returns the value in the same column of another row.
HOUR(serial_number)
    DateTime: Returns the hour (0-23) of a time.
HSTACK(array1, [array2], ...)
    Lookup: Places arrays side by side.
HYPERLINK(link_location, [friendly_name])
    Information: Creates a link; the cell shows the friendly name, or the link itself.
HYPGEOM.DIST(sample_s, number_sample, population_s, number_pop, cumulative)
    Statistical: Hypergeometric probability.
HYPGEOMDIST(sample_s, number_sample, population_s, number_pop)
    Compatibility: Hypergeometric probability of an exact count.
IF(logical_test, [value_if_true], [value_if_false])
    Logical: Returns one value when a condition is TRUE and another when it is FALSE.
IFERROR(value, value_if_error)
    Logical: Returns a fallback when the value is an error, otherwise the value.
IFNA(value, value_if_na)
    Logical: Returns a fallback when the value is #N/A, otherwise the value.
IFS(logical_test1, value_if_true1, ...)
    Logical: Returns the value paired with the first condition that is TRUE.
IMABS(inumber)
    Engineering: Absolute value (modulus) of a complex number.
IMAGINARY(inumber)
    Engineering: Imaginary coefficient of a complex number.
IMARGUMENT(inumber)
    Engineering: Angle of a complex number in radians.
IMCONJUGATE(inumber)
    Engineering: Complex conjugate of a complex number.
IMCOS(inumber)
    Engineering: Cosine of a complex number.
IMCOSH(inumber)
    Engineering: Hyperbolic cosine of a complex number.
IMCOT(inumber)
    Engineering: Cotangent of a complex number.
IMCSC(inumber)
    Engineering: Cosecant of a complex number.
IMCSCH(inumber)
    Engineering: Hyperbolic cosecant of a complex number.
IMDIV(inumber1, inumber2)
    Engineering: Quotient of two complex numbers.
IMEXP(inumber)
    Engineering: Exponential of a complex number.
IMLN(inumber)
    Engineering: Natural logarithm of a complex number.
IMLOG10(inumber)
    Engineering: Base-10 logarithm of a complex number.
IMLOG2(inumber)
    Engineering: Base-2 logarithm of a complex number.
IMPOWER(inumber, number)
    Engineering: Raises a complex number to a power.
IMPRODUCT(inumber1, [inumber2], ...)
    Engineering: Product of complex numbers.
IMREAL(inumber)
    Engineering: Real coefficient of a complex number.
IMSEC(inumber)
    Engineering: Secant of a complex number.
IMSECH(inumber)
    Engineering: Hyperbolic secant of a complex number.
IMSIN(inumber)
    Engineering: Sine of a complex number.
IMSINH(inumber)
    Engineering: Hyperbolic sine of a complex number.
IMSQRT(inumber)
    Engineering: Square root of a complex number.
IMSUB(inumber1, inumber2)
    Engineering: Difference of two complex numbers.
IMSUM(inumber1, [inumber2], ...)
    Engineering: Sum of complex numbers.
IMTAN(inumber)
    Engineering: Tangent of a complex number.
INDEX(array, row_num, [column_num], [area_num])
    Lookup: Returns the element, row or column of an array at the given position.
INDIRECT(ref_text, [a1])
    Lookup: The reference named by a text string.
INFO(type_text)
    Information: Returns information about the operating environment.
INT(number)
    MathTrig: Rounds a number down to the nearest integer.
INTERCEPT(known_ys, known_xs)
    Statistical: Y-intercept of the least-squares regression line.
INTRATE(settlement, maturity, investment, redemption, [basis])
    Financial: Interest rate of a fully invested security.
IPMT(rate, per, nper, pv, [fv], [type])
    Financial: Interest part of a given period's payment.
IRR(values, [guess])
    Financial: Internal rate of return of periodic cash flows.
ISBLANK(value)
    Information: TRUE when the value refers to an empty cell.
ISERR(value)
    Information: TRUE when the value is any error other than #N/A.
ISERROR(value)
    Information: TRUE when the value is any error.
ISEVEN(number)
    Information: TRUE when the integer part of a number is even.
ISFORMULA(reference)
    Information: TRUE when the cell has a formula.
ISLOGICAL(value)
    Information: TRUE when the value is TRUE or FALSE.
ISNA(value)
    Information: TRUE when the value is the #N/A error.
ISNONTEXT(value)
    Information: TRUE when the value is anything other than text.
ISNUMBER(value)
    Information: TRUE when the value is a number.
ISO.CEILING(number, [significance])
    MathTrig: Rounds a number toward positive infinity to a multiple.
ISODD(number)
    Information: TRUE when the integer part of a number is odd.
ISOMITTED(argument)
    Information: TRUE when a LAMBDA argument was left out.
ISOWEEKNUM(date)
    DateTime: Returns the ISO 8601 week number of a date.
ISPMT(rate, per, nper, pv)
    Financial: Interest paid in a period of a loan with even principal payments.
ISREF(value)
    Information: TRUE for references.
ISTEXT(value)
    Information: TRUE when the value is text.
JIS(text)
    Text: Converts half-width characters to full-width (no change in this locale).
KURT(number1, [number2], ...)
    Statistical: Excess kurtosis of a sample.
LAMBDA([parameter1, ...], calculation)
    Logical: Creates a reusable custom function.
LARGE(array, k)
    Statistical: The k-th largest number in a data set.
LCM(number1, [number2], ...)
    MathTrig: Least common multiple of integers.
LEFT(text, [num_chars])
    Text: Returns the first characters of a text.
LEFTB(text, [num_bytes])
    Text: Byte version of LEFT (same as LEFT for single-byte text).
LEN(text)
    Text: Counts the characters in a text.
LENB(text)
    Text: Byte version of LEN (same as LEN for single-byte text).
LET(name1, value1, ..., calculation)
    Logical: Names intermediate results.
LINEST(known_ys, [known_xs], [const], [stats])
    Statistical: Least-squares line coefficients and optional regression statistics.
LN(number)
    MathTrig: Natural logarithm.
LOG(number, [base])
    MathTrig: Logarithm to the given base (10 by default).
LOG10(number)
    MathTrig: Base-10 logarithm.
LOGEST(known_ys, [known_xs], [const], [stats])
    Statistical: Exponential curve coefficients and optional regression statistics.
LOGINV(probability, mean, standard_dev)
    Compatibility: Inverse of the cumulative lognormal distribution.
LOGNORM.DIST(x, mean, standard_dev, cumulative)
    Statistical: Lognormal density or probability.
LOGNORM.INV(probability, mean, standard_dev)
    Statistical: Inverse of the cumulative lognormal distribution.
LOGNORMDIST(x, mean, standard_dev)
    Compatibility: Cumulative lognormal probability.
LOOKUP(lookup_value, lookup_vector, [result_vector])
    Lookup: Approximate lookup in a sorted vector or the first row/column of an array.
LOWER(text)
    Text: Converts text to lower case.
MAKEARRAY(rows, cols, lambda)
    Logical: Builds an array from a LAMBDA.
MAP(array1, ..., lambda)
    Logical: Applies a LAMBDA to each value.
MATCH(lookup_value, lookup_array, [match_type])
    Lookup: Returns the 1-based position of a value in a row or column.
MAX(number1, [number2], ...)
    Statistical: Largest number (0 when there are none).
MAXA(value1, [value2], ...)
    Statistical: Largest value counting text as 0 and logicals as 1/0.
MAXIFS(max_range, criteria_range1, criteria1, ...)
    Statistical: Largest value among cells that meet every condition.
MDETERM(array)
    MathTrig: Determinant of a square matrix.
MDURATION(settlement, maturity, coupon, yld, frequency, [basis])
    Financial: Modified duration of a security with periodic interest.
MEDIAN(number1, [number2], ...)
    Statistical: Middle value of the numbers.
MID(text, start_num, num_chars)
    Text: Returns characters from the middle of a text.
MIDB(text, start_num, num_bytes)
    Text: Byte version of MID (same as MID for single-byte text).
MIN(number1, [number2], ...)
    Statistical: Smallest number (0 when there are none).
MINA(value1, [value2], ...)
    Statistical: Smallest value counting text as 0 and logicals as 1/0.
MINIFS(min_range, criteria_range1, criteria1, ...)
    Statistical: Smallest value among cells that meet every condition.
MINUTE(serial_number)
    DateTime: Returns the minute (0-59) of a time.
MINVERSE(array)
    MathTrig: Inverse of a square matrix.
MIRR(values, finance_rate, reinvest_rate)
    Financial: Modified internal rate of return using separate borrow and reinvest rates.
MMULT(array1, array2)
    MathTrig: Matrix product of two arrays.
MOD(number, divisor)
    MathTrig: Remainder of a division, with the sign of the divisor.
MODE(number1, [number2], ...)
    Compatibility: Most frequently occurring number.
MODE.MULT(number1, [number2], ...)
    Statistical: Vertical array of all the most frequent numbers.
MODE.SNGL(number1, [number2], ...)
    Statistical: Most frequently occurring number.
MONTH(serial_number)
    DateTime: Returns the month (1-12) of a date.
MROUND(number, multiple)
    MathTrig: Rounds a number to the nearest multiple.
MULTINOMIAL(number1, [number2], ...)
    MathTrig: Ratio of the factorial of a sum to the product of factorials.
MUNIT(dimension)
    MathTrig: Identity matrix of the given size.
N(value)
    Information: Converts a value to a number: numbers stay, TRUE is 1, everything else is 0.
NA()
    Information: Returns the #N/A error value.
NEGBINOM.DIST(number_f, number_s, probability_s, cumulative)
    Statistical: Negative binomial probability.
NEGBINOMDIST(number_f, number_s, probability_s)
    Compatibility: Negative binomial probability.
NETWORKDAYS(start_date, end_date, [holidays])
    DateTime: Counts working days (Monday to Friday) between two dates, excluding holidays.
NETWORKDAYS.INTL(start_date, end_date, [weekend], [holidays])
    DateTime: Counts working days between two dates with a custom weekend, excluding holidays.
NOMINAL(effect_rate, npery)
    Financial: Nominal annual rate from an effective rate and compounding periods.
NORM.DIST(x, mean, standard_dev, cumulative)
    Statistical: Normal distribution density or cumulative probability.
NORM.INV(probability, mean, standard_dev)
    Statistical: Inverse of the normal cumulative distribution.
NORM.S.DIST(z, cumulative)
    Statistical: Standard normal density or cumulative probability.
NORM.S.INV(probability)
    Statistical: Inverse of the standard normal cumulative distribution.
NORMDIST(x, mean, standard_dev, cumulative)
    Compatibility: Normal distribution density or cumulative probability.
NORMINV(probability, mean, standard_dev)
    Compatibility: Inverse of the normal cumulative distribution.
NORMSDIST(z)
    Compatibility: Standard normal cumulative probability.
NORMSINV(probability)
    Compatibility: Inverse of the standard normal cumulative distribution.
NOT(logical)
    Logical: Reverses a logical value.
NOW()
    DateTime: Returns the current date and time.
NPER(rate, pmt, pv, [fv], [type])
    Financial: Number of periods needed to pay off or accumulate an amount.
NPV(rate, value1, [value2], ...)
    Financial: Net present value of periodic cash flows at a discount rate.
NUMBERVALUE(text, [decimal_separator], [group_separator])
    Text: Converts text to a number using the given decimal and group separators.
OCT2BIN(number, [places])
    Engineering: Converts an octal number to binary.
OCT2DEC(number)
    Engineering: Converts an octal number to decimal.
OCT2HEX(number, [places])
    Engineering: Converts an octal number to hexadecimal.
ODD(number)
    MathTrig: Rounds away from zero to the nearest odd integer.
ODDFPRICE(settlement, maturity, issue, first_coupon, rate, yld, redemption, frequency, [basis])
    Financial: Price per 100 face value of a security with an odd first period.
ODDFYIELD(settlement, maturity, issue, first_coupon, rate, pr, redemption, frequency, [basis])
    Financial: Yield of a security with an odd first period.
ODDLPRICE(settlement, maturity, last_interest, rate, yld, redemption, frequency, [basis])
    Financial: Price per 100 face value of a security with an odd last period.
ODDLYIELD(settlement, maturity, last_interest, rate, pr, redemption, frequency, [basis])
    Financial: Yield of a security with an odd last period.
OFFSET(reference, rows, cols, [height], [width])
    Lookup: A reference shifted from a starting point.
OR(logical1, [logical2], ...)
    Logical: TRUE when at least one argument is TRUE.
PDURATION(rate, pv, fv)
    Financial: Periods needed for an investment to grow to a target value.
PEARSON(array1, array2)
    Statistical: Pearson product-moment correlation coefficient.
PERCENTILE(array, k)
    Compatibility: k-th percentile, k from 0 to 1 inclusive.
PERCENTILE.EXC(array, k)
    Statistical: k-th percentile, k strictly between 0 and 1.
PERCENTILE.INC(array, k)
    Statistical: k-th percentile, k from 0 to 1 inclusive.
PERCENTOF(data_subset, data_all)
    MathTrig: The sum of a subset as a fraction of the sum of all the values.
PERCENTRANK(array, x, [significance])
    Compatibility: Relative standing of a value as a fraction of the data set.
PERCENTRANK.EXC(array, x, [significance])
    Statistical: Relative standing of a value strictly between 0 and 1.
PERCENTRANK.INC(array, x, [significance])
    Statistical: Relative standing of a value from 0 to 1 inclusive.
PERMUT(number, number_chosen)
    Statistical: Number of ordered selections without repetition.
PERMUTATIONA(number, number_chosen)
    Statistical: Number of ordered selections with repetition.
PHI(x)
    Statistical: Standard normal density.
PHONETIC(reference)
    Text: Returns the phonetic (furigana) text; here the text itself.
PI()
    MathTrig: The constant pi to 15 digits.
PIVOTBY(row_fields, col_fields, values, function, [field_headers], [row_total_depth], [row_sort_order], [col_total_depth], [col_sort_order], [filter_array], [relative_to])
    Lookup: Builds a summary table grouping values by row and column fields.
PMT(rate, nper, pv, [fv], [type])
    Financial: Periodic payment for a loan or annuity with constant payments and rate.
POISSON(x, mean, cumulative)
    Compatibility: Poisson probability.
POISSON.DIST(x, mean, cumulative)
    Statistical: Poisson probability.
POWER(number, power)
    MathTrig: Raises a number to a power.
PPMT(rate, per, nper, pv, [fv], [type])
    Financial: Principal part of a given period's payment.
PRICE(settlement, maturity, rate, yld, redemption, frequency, [basis])
    Financial: Price per 100 face value of a security paying periodic interest.
PRICEDISC(settlement, maturity, discount, redemption, [basis])
    Financial: Price per 100 face value of a discounted security.
PRICEMAT(settlement, maturity, issue, rate, yld, [basis])
    Financial: Price per 100 face value of a security paying interest at maturity.
PROB(x_range, prob_range, lower_limit, [upper_limit])
    Statistical: Probability that values fall between two limits.
PRODUCT(number1, [number2], ...)
    MathTrig: Multiplies all the numbers in the arguments.
PROPER(text)
    Text: Capitalises the first letter of each word and lower-cases the rest.
PV(rate, nper, pmt, [fv], [type])
    Financial: Present value of a series of equal future payments.
QUARTILE(array, quart)
    Compatibility: Quartile (0–4) of a data set.
QUARTILE.EXC(array, quart)
    Statistical: Quartile (1–3) of a data set, exclusive method.
QUARTILE.INC(array, quart)
    Statistical: Quartile (0–4) of a data set, inclusive method.
QUOTIENT(numerator, denominator)
    MathTrig: Integer part of a division.
RADIANS(angle)
    MathTrig: Converts degrees to radians.
RAND()
    MathTrig: A random number between 0 and 1, recalculated every time.
RANDARRAY([rows], [columns], [min], [max], [whole_number])
    MathTrig: Builds an array of random numbers in a range.
RANDBETWEEN(bottom, top)
    MathTrig: A random integer between two bounds, inclusive.
RANK(number, ref, [order])
    Compatibility: Rank of a number within a list.
RANK.AVG(number, ref, [order])
    Statistical: Rank of a number within a list; ties get the average rank.
RANK.EQ(number, ref, [order])
    Statistical: Rank of a number within a list; ties share the top rank.
RATE(nper, pmt, pv, [fv], [type], [guess])
    Financial: Interest rate per period of an annuity, found iteratively.
RECEIVED(settlement, maturity, investment, discount, [basis])
    Financial: Amount received at maturity for a fully invested security.
REDUCE(initial_value, array, lambda)
    Logical: Accumulates an array into one value.
REGEXEXTRACT(text, pattern, [return_mode], [case_sensitivity])
    Text: Extracts the first match, all matches or the capture groups of a regular expression.
REGEXREPLACE(text, pattern, replacement, [occurrence], [case_sensitivity])
    Text: Replaces matches of a regular expression, all of them or a chosen occurrence.
REGEXTEST(text, pattern, [case_sensitivity])
    Text: TRUE when a regular expression matches somewhere in the text.
REPLACE(old_text, start_num, num_chars, new_text)
    Text: Replaces part of a text by position.
REPLACEB(old_text, start_num, num_bytes, new_text)
    Text: Byte version of REPLACE.
REPT(text, number_times)
    Text: Repeats a text a given number of times.
RIGHT(text, [num_chars])
    Text: Returns the last characters of a text.
RIGHTB(text, [num_bytes])
    Text: Byte version of RIGHT (same as RIGHT for single-byte text).
ROMAN(number, [form])
    MathTrig: Converts a number to Roman numerals in one of five styles.
ROUND(number, num_digits)
    MathTrig: Rounds a number to a given number of digits, halves away from zero.
ROUNDDOWN(number, num_digits)
    MathTrig: Rounds a number toward zero to a given number of digits.
ROUNDUP(number, num_digits)
    MathTrig: Rounds a number away from zero to a given number of digits.
ROW([reference])
    Lookup: Row number of a reference.
ROWS(array)
    Lookup: Counts the rows in an array or range.
RRI(nper, pv, fv)
    Financial: Equivalent interest rate for the growth of an investment.
RSQ(known_ys, known_xs)
    Statistical: Square of the correlation coefficient.
SCAN(initial_value, array, lambda)
    Logical: Running accumulation of an array.
SEARCH(find_text, within_text, [start_num])
    Text: Finds the position of one text in another, ignoring case and allowing wildcards.
SEARCHB(find_text, within_text, [start_num])
    Text: Byte version of SEARCH.
SEC(number)
    MathTrig: Secant of an angle in radians.
SECH(number)
    MathTrig: Hyperbolic secant.
SECOND(serial_number)
    DateTime: Returns the second (0-59) of a time.
SEQUENCE(rows, [columns], [start], [step])
    MathTrig: Builds an array of evenly stepped numbers.
SERIESSUM(x, n, m, coefficients)
    MathTrig: Sum of a power series.
SHEET([value])
    Information: Sheet number.
SHEETS([reference])
    Information: Number of sheets.
SIGN(number)
    MathTrig: 1 for positive, -1 for negative and 0 for zero.
SIN(number)
    MathTrig: Sine of an angle in radians.
SINH(number)
    MathTrig: Hyperbolic sine.
SKEW(number1, [number2], ...)
    Statistical: Sample skewness.
SKEW.P(number1, [number2], ...)
    Statistical: Population skewness.
SLN(cost, salvage, life)
    Financial: Straight-line depreciation for one period.
SLOPE(known_ys, known_xs)
    Statistical: Slope of the least-squares regression line.
SMALL(array, k)
    Statistical: The k-th smallest number in a data set.
SORT(array, [sort_index], [sort_order], [by_col])
    Lookup: Sorts the rows (or columns) of an array by one or more of its columns.
SORTBY(array, by_array1, [sort_order1], ...)
    Lookup: Sorts an array by the values of other arrays of matching size.
SQRT(number)
    MathTrig: Positive square root.
SQRTPI(number)
    MathTrig: Square root of the number times pi.
STANDARDIZE(x, mean, standard_dev)
    Statistical: Z-score of a value.
STDEV(number1, [number2], ...)
    Compatibility: Sample standard deviation.
STDEV.P(number1, [number2], ...)
    Statistical: Population standard deviation.
STDEV.S(number1, [number2], ...)
    Statistical: Sample standard deviation.
STDEVA(value1, [value2], ...)
    Statistical: Sample standard deviation counting text as 0 and logicals as 1/0.
STDEVP(number1, [number2], ...)
    Compatibility: Population standard deviation.
STDEVPA(value1, [value2], ...)
    Statistical: Population standard deviation counting text as 0 and logicals as 1/0.
STEYX(known_ys, known_xs)
    Statistical: Standard error of predicted y values in a regression.
SUBSTITUTE(text, old_text, new_text, [instance_num])
    Text: Replaces occurrences of one text with another, optionally only a given occurrence.
SUBTOTAL(function_num, ref1, ...)
    MathTrig: A subtotal that can skip hidden rows.
SUM(number1, [number2], ...)
    MathTrig: Adds all the numbers in the arguments.
SUMIF(range, criteria, [sum_range])
    MathTrig: Adds the cells that meet a condition.
SUMIFS(sum_range, criteria_range1, criteria1, ...)
    MathTrig: Adds the cells that meet every condition.
SUMPRODUCT(array1, [array2], ...)
    MathTrig: Multiplies matching elements of equally sized arrays and adds the products.
SUMSQ(number1, [number2], ...)
    MathTrig: Adds the squares of the numbers.
SUMX2MY2(array_x, array_y)
    MathTrig: Sums the differences of squares of matching elements.
SUMX2PY2(array_x, array_y)
    MathTrig: Sums the sums of squares of matching elements.
SUMXMY2(array_x, array_y)
    MathTrig: Sums the squared differences of matching elements.
SWITCH(expression, value1, result1, [default_or_value2, result2], ...)
    Logical: Compares an expression with a list of values and returns the result paired with the first match.
SYD(cost, salvage, life, per)
    Financial: Sum-of-years'-digits depreciation for a period.
T(value)
    Text: Returns the value if it is text, otherwise empty text.
T.DIST(x, deg_freedom, cumulative)
    Statistical: Student's t density or left-tailed probability.
T.DIST.2T(x, deg_freedom)
    Statistical: Two-tailed Student's t probability.
T.DIST.RT(x, deg_freedom)
    Statistical: Right-tailed Student's t probability.
T.INV(probability, deg_freedom)
    Statistical: Left-tailed inverse of Student's t distribution.
T.INV.2T(probability, deg_freedom)
    Statistical: Two-tailed inverse of Student's t distribution.
T.TEST(array1, array2, tails, type)
    Statistical: Probability from Student's t-test.
TAKE(array, rows, [columns])
    Lookup: Keeps rows or columns from the start (or end) of an array.
TAN(number)
    MathTrig: Tangent of an angle in radians.
TANH(number)
    MathTrig: Hyperbolic tangent.
TBILLEQ(settlement, maturity, discount)
    Financial: Bond-equivalent yield of a Treasury bill.
TBILLPRICE(settlement, maturity, discount)
    Financial: Price per 100 face value of a Treasury bill.
TBILLYIELD(settlement, maturity, pr)
    Financial: Yield of a Treasury bill.
TDIST(x, deg_freedom, tails)
    Compatibility: One- or two-tailed Student's t probability.
TEXT(value, format_text)
    Text: Formats a number as text.
TEXTAFTER(text, delimiter, [instance_num], [match_mode], [match_end], [if_not_found])
    Text: Returns the text that comes after a delimiter.
TEXTBEFORE(text, delimiter, [instance_num], [match_mode], [match_end], [if_not_found])
    Text: Returns the text that comes before a delimiter.
TEXTJOIN(delimiter, ignore_empty, text1, [text2], ...)
    Text: Joins text from values and ranges with a delimiter, optionally skipping empty items.
TEXTSPLIT(text, col_delimiter, [row_delimiter], [ignore_empty], [match_mode], [pad_with])
    Text: Splits text into a grid of columns and rows at the given delimiters.
TIME(hour, minute, second)
    DateTime: Builds a time (a fraction of a day) from hours, minutes and seconds.
TIMEVALUE(time_text)
    DateTime: Converts a time written as text into a fraction of a day.
TINV(probability, deg_freedom)
    Compatibility: Two-tailed inverse of Student's t distribution.
TOCOL(array, [ignore], [scan_by_column])
    Lookup: Flattens an array into a single column, optionally skipping blanks or errors.
TODAY()
    DateTime: Returns the current date.
TOROW(array, [ignore], [scan_by_column])
    Lookup: Flattens an array into a single row, optionally skipping blanks or errors.
TRANSPOSE(array)
    Lookup: Swaps the rows and columns of an array.
TREND(known_ys, [known_xs], [new_xs], [const])
    Statistical: Values along a least-squares linear fit.
TRIM(text)
    Text: Removes leading and trailing spaces and collapses runs of spaces to one.
TRIMMEAN(array, percent)
    Statistical: Mean after trimming a fraction of points from both ends.
TRIMRANGE(range, [trim_rows], [trim_cols])
    Lookup: A range or array without its blank outer rows and columns.
TRUE()
    Logical: Returns the logical value TRUE.
TRUNC(number, [num_digits])
    MathTrig: Cuts off the fractional part of a number at the given digits.
TTEST(array1, array2, tails, type)
    Compatibility: Probability from Student's t-test.
TYPE(value)
    Information: Returns a code for the kind of value: 1 number, 2 text, 4 logical, 16 error, 64 array.
UNICHAR(number)
    Text: Returns the character for a Unicode code point.
UNICODE(text)
    Text: Returns the Unicode code point of the first character of a text.
UNIQUE(array, [by_col], [exactly_once])
    Lookup: Returns the distinct rows or columns of an array.
UPPER(text)
    Text: Converts text to upper case.
USDOLLAR(number, [decimals])
    Compatibility: Formats a number as currency text, like DOLLAR.
VALUE(text)
    Text: Converts text that looks like a number, date or time into a number.
VALUETOTEXT(value, [format])
    Text: Converts any value to text, optionally in strict (quoted) form.
VAR(number1, [number2], ...)
    Compatibility: Sample variance.
VAR.P(number1, [number2], ...)
    Statistical: Population variance.
VAR.S(number1, [number2], ...)
    Statistical: Sample variance.
VARA(value1, [value2], ...)
    Statistical: Sample variance counting text as 0 and logicals as 1/0.
VARP(number1, [number2], ...)
    Compatibility: Population variance.
VARPA(value1, [value2], ...)
    Statistical: Population variance counting text as 0 and logicals as 1/0.
VDB(cost, salvage, life, start_period, end_period, [factor], [no_switch])
    Financial: Declining-balance depreciation over any span of periods, switching to straight line.
VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
    Lookup: Finds a value in the first column of a table and returns the value in the same row of another column.
VSTACK(array1, [array2], ...)
    Lookup: Stacks arrays on top of each other.
WEBSERVICE(url)
    Web: Fetches data from a web service (not available; returns #VALUE!).
WEEKDAY(serial_number, [return_type])
    DateTime: Returns the day of the week of a date as a number.
WEEKNUM(serial_number, [return_type])
    DateTime: Returns the week number of a date within its year.
WEIBULL(x, alpha, beta, cumulative)
    Compatibility: Weibull density or probability.
WEIBULL.DIST(x, alpha, beta, cumulative)
    Statistical: Weibull density or probability.
WORKDAY(start_date, days, [holidays])
    DateTime: Returns the date a number of working days before or after a date.
WORKDAY.INTL(start_date, days, [weekend], [holidays])
    DateTime: Returns the date a number of working days away with a custom weekend.
WRAPCOLS(vector, wrap_count, [pad_with])
    Lookup: Breaks a row or column into columns of the given length.
WRAPROWS(vector, wrap_count, [pad_with])
    Lookup: Breaks a row or column into rows of the given length.
XIRR(values, dates, [guess])
    Financial: Internal rate of return of cash flows on specific dates.
XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
    Lookup: Searches a row or column and returns the matching item, row or column from another array.
XMATCH(lookup_value, lookup_array, [match_mode], [search_mode])
    Lookup: Returns the position of a value in a row or column with flexible match and search modes.
XNPV(rate, values, dates)
    Financial: Net present value of cash flows on specific dates.
XOR(logical1, [logical2], ...)
    Logical: TRUE when an odd number of arguments are TRUE.
YEAR(serial_number)
    DateTime: Returns the year of a date.
YEARFRAC(start_date, end_date, [basis])
    DateTime: Returns the fraction of a year between two dates under a day-count basis.
YIELD(settlement, maturity, rate, pr, redemption, frequency, [basis])
    Financial: Yield of a security paying periodic interest.
YIELDDISC(settlement, maturity, pr, redemption, [basis])
    Financial: Annual yield of a discounted security.
YIELDMAT(settlement, maturity, issue, rate, pr, [basis])
    Financial: Annual yield of a security paying interest at maturity.
Z.TEST(array, x, [sigma])
    Statistical: One-tailed probability of a z-test.
ZTEST(array, x, [sigma])
    Compatibility: One-tailed probability of a z-test.
```
